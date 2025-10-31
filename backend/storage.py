# backend/storage.py
"""
Storage layer with in-memory default, optional SQLite backend, and Aurora MySQL backend.

Set STORAGE_BACKEND=sqlite for SQLite.
Set STORAGE_BACKEND=aurora for Aurora MySQL.

Exposed API (used by main.py):
- start_session(session_id, source=None)
- session_exists(session_id) -> bool

- save_demographics(session_id, payload, recaptcha_verification=None)
- mark_recaptcha_result(session_id, endpoint, ok)

- set_assignment(session_id, passage_ids)
- get_assignment(session_id) -> list[str] | None
- set_source_assignment(session_id, mapping)
- get_source_for(session_id, passage_id) -> str | None

- save_mcq_submission(...)
- get_mcq_submission(session_id, passage_id) -> dict | None
- save_posttask_feedback(session_id, passage_uid, ratings)

- init_vocab(session_id, size)                         # progress only (in-memory)
- advance_vocab(session_id, item_id, is_word, rt_ms,   # progress only (in-memory)
                is_correct: bool)
- get_vocab_progress(session_id)                       # progress only (in-memory)
- save_vocab_final(session_id, trials)                 # ONE final row persisted (list of {token,user_answer})

- final_check(session_id, data, recaptcha_verification=None)

- log_total_participation_time(session_id, finished_at_ms=None) -> { ... }
- log_total_task_time(session_id, bucket, elapsed_ms) -> { ... }
- log_reading_comprehension_details(session_id, event) -> { ... }
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any, DefaultDict, Dict, List, Optional
import os
import time
import json

# -----------------------------
# Config helpers (env + optional SSM)
# -----------------------------
try:
    import boto3  
except Exception:  
    boto3 = None

from functools import lru_cache

@lru_cache()
def _get_ssm_param(name: str, decrypt: bool = True) -> Optional[str]:
    if boto3 is None:
        return None
    region = os.getenv("AWS_REGION") or os.getenv("AWS_DEFAULT_REGION") or "us-east-1"
    try:
        ssm = boto3.client("ssm", region_name=region)
        return ssm.get_parameter(Name=name, WithDecryption=decrypt)["Parameter"]["Value"]
    except Exception:
        return None

def _cfg(env_key: str, default: Optional[str] = None, ssm_path: Optional[str] = None, secure: bool = False) -> Optional[str]:
    v = os.getenv(env_key)
    if v:
        return v
    if ssm_path:
        vv = _get_ssm_param(ssm_path, decrypt=secure)
        if vv:
            return vv
    return default

# Backend selection
STORAGE_BACKEND = (_cfg("STORAGE_BACKEND", default="sqlite", ssm_path="/requesta/STORAGE_BACKEND")).lower()
SQLITE_PATH = _cfg("SQLITE_PATH", default="study_data.db")

def _now_ms() -> int:
    return int(time.time() * 1000)

DEFAULT_BUCKETS = {
    "consent": 0,
    "demographic": 0,
    "reading_instruction": 0,
    "reading_task1": 0,
    "survey_task1": 0,
    "reading_task2": 0,
    "survey_task2": 0,
    "reading_task3": 0,
    "survey_task3": 0,
    "vocabulary": 0,
}

# Debounce / clamp constants for RC and attention logging
_RC_SPURIOUS_BLUR_MAX_MS = 250
_RC_MIN_SEG_MS = 40                # drop micro flutter
_RC_MAX_SEG_MS = 30 * 60 * 1000    # cap single segment to 30 minutes
_RC_MERGE_GAP_MS = 500             # merge identical adjacent segments if gap <= 500ms
_ATTENTION_MAX_INC_MS = 4 * 60 * 60 * 1000  # cap single increment to 4h

# =====================================================================
# SQLITE BACKEND 
# =====================================================================
if STORAGE_BACKEND == "sqlite":
    import sqlite3
    import threading

    SESSIONS: Dict[str, Dict[str, Any]] = {}
    RC_EVENTS: DefaultDict[str, List[Dict[str, Any]]] = defaultdict(list)

    _LOCK = threading.RLock()
    _conn = sqlite3.connect(SQLITE_PATH or "study_data.db", check_same_thread=False)
    with _conn:
        _conn.execute("PRAGMA journal_mode=WAL;")
        _conn.execute("PRAGMA synchronous=NORMAL;")
        _conn.execute("PRAGMA foreign_keys=ON;")
        _conn.execute("""
            CREATE TABLE IF NOT EXISTS kv (
              pk TEXT NOT NULL,
              sk TEXT NOT NULL,
              content_json TEXT NOT NULL,
              ts INTEGER NOT NULL,
              PRIMARY KEY (pk, sk)
            )
        """)

    def _pk(session_id: str) -> str:
        return f"{session_id}"

    def _sk(kind: str, suffix: str | None = None) -> str:
        return f"{kind}#{suffix}" if suffix else kind

    def _get(pk: str, sk: str) -> Optional[Dict[str, Any]]:
        with _LOCK:
            cur = _conn.execute("SELECT content_json FROM kv WHERE pk=? AND sk=?", (pk, sk))
            row = cur.fetchone()
        if not row:
            return None
        return json.loads(row[0])

    def _put(pk: str, sk: str, content: Dict[str, Any]) -> None:
        blob = json.dumps(content, separators=(",", ":"), ensure_ascii=False)
        ts = _now_ms()
        with _LOCK:
            _conn.execute(
                "INSERT INTO kv (pk, sk, content_json, ts) VALUES (?, ?, ?, ?) "
                "ON CONFLICT(pk, sk) DO UPDATE SET content_json=excluded.content_json, ts=excluded.ts",
                (pk, sk, blob, ts)
            )
            _conn.commit()

    def start_session(session_id: str, source: str | None = None) -> None:
        SESSIONS[session_id] = {"created_at": time.time(), "source": source, "consent": True}
        profile = {"created_at_ms": _now_ms(), "source": source, "consent": True}
        _put(_pk(session_id), _sk("PROFILE"), profile)

    def session_exists(session_id: str) -> bool:
        if session_id in SESSIONS:
            return True
        pk = _pk(session_id)
        with _LOCK:
            cur = _conn.execute("SELECT 1 FROM kv WHERE pk=? AND sk='PROFILE' LIMIT 1", (pk,))
            found = cur.fetchone() is not None
        if found:
            SESSIONS.setdefault(session_id, {})
        return found

    def save_demographics(session_id: str, payload: Dict[str, Any], recaptcha_verification: str | None = None) -> None:
        rec = dict(payload)
        if recaptcha_verification in ("yes", "no"):
            rec["recaptcha_verification"] = recaptcha_verification
        row = {"payload": rec, "server_ts": _now_ms()}
        _put(_pk(session_id), _sk("DEMOGRAPHICS"), row)

    def mark_recaptcha_result(session_id: str, endpoint: str, ok: bool) -> None:
        prof = _get(_pk(session_id), _sk("PROFILE")) or {}
        prof[f"recaptcha_{endpoint}"] = "yes" if ok else "no"
        prof["recaptcha_ts"] = _now_ms()
        _put(_pk(session_id), _sk("PROFILE"), prof)
        SESSIONS.setdefault(session_id, {}).update({"recaptcha_ts": prof["recaptcha_ts"]})

    def set_assignment(session_id: str, passage_ids: List[str]) -> None:
        row = _get(_pk(session_id), _sk("ASSIGNMENT")) or {}
        row["passage_ids"] = list(passage_ids)
        row["server_ts"] = _now_ms()
        _put(_pk(session_id), _sk("ASSIGNMENT"), row)

    def get_assignment(session_id: str) -> List[str] | None:
        row = _get(_pk(session_id), _sk("ASSIGNMENT")) or {}
        return row.get("passage_ids")

    def set_source_assignment(session_id: str, mapping: Dict[str, str]) -> None:
        row = _get(_pk(session_id), _sk("ASSIGNMENT")) or {}
        row["sources"] = dict(mapping)
        row["server_ts"] = _now_ms()
        _put(_pk(session_id), _sk("ASSIGNMENT"), row)

    def get_source_for(session_id: str, passage_id: str) -> Optional[str]:
        row = _get(_pk(session_id), _sk("ASSIGNMENT")) or {}
        srcs = row.get("sources") or {}
        return srcs.get(passage_id)

    def save_mcq_submission(session_id: str, passage_id: str, passage_uid: str, source: str,
                            per_question: List[Dict[str, Any]], score: int, meta: Dict[str, Any]) -> None:
        item = {"passage_uid": passage_uid, "source": source, "per_question": per_question,
                "score": score, "meta": meta, "ts": _now_ms()}
        _put(_pk(session_id), _sk("MCQ", passage_id), item)

    def get_mcq_submission(session_id: str, passage_id: str) -> Optional[Dict[str, Any]]:
        return _get(_pk(session_id), _sk("MCQ", passage_id))

    def save_posttask_feedback(session_id: str, passage_uid: str, ratings: Dict[str, int]) -> None:
        key_pk = _pk(session_id)
        key_sk = _sk("POSTTASK", passage_uid)
        existing = _get(key_pk, key_sk) or {"ratings": {}}
        merged = dict(existing.get("ratings") or {})
        merged.update(ratings)
        _put(key_pk, key_sk, {"ratings": merged, "ts": _now_ms()})

    VOCAB_PROGRESS: Dict[str, Dict[str, Any]] = defaultdict(dict)

    def init_vocab(session_id: str, size: int) -> None:
        VOCAB_PROGRESS[session_id] = {"index": 0, "size": size}

    def advance_vocab(session_id: str, item_id: str, is_word: bool, rt_ms: int | None, is_correct: bool) -> None:
        prog = VOCAB_PROGRESS[session_id]
        prog["index"] = int(prog.get("index", 0)) + 1

    def get_vocab_progress(session_id: str) -> Dict[str, Any]:
        return VOCAB_PROGRESS.get(session_id, {"index": 0, "size": 0})

    def save_vocab_final(session_id: str, trials: List[Dict[str, Any]]) -> None:
        _put(_pk(session_id), _sk("VOCAB"), {"trials": trials, "ts": _now_ms()})

    def final_check(session_id: str, data: Dict[str, Any], recaptcha_verification: str | None = None) -> None:
        prof = _get(_pk(session_id), _sk("PROFILE")) or {}
        rec = {
            "used_ai_tools": data.get("used_ai_tools"),
            "tools": list(data.get("tools") or []),
            "other_tool": (data.get("other_tool") or "").strip(),
            "server_ts": _now_ms(),
        }
        if recaptcha_verification in ("yes", "no"):
            rec["recaptcha_verification"] = recaptcha_verification
        prof["final_check"] = rec
        _put(_pk(session_id), _sk("PROFILE"), prof)

    def log_total_participation_time(session_id: str, finished_at_ms: Optional[int] = None) -> Dict[str, Any]:
        prof = _get(_pk(session_id), _sk("PROFILE"))
        if not prof:
            raise ValueError("Session not found.")
        start_ms = int(prof.get("created_at_ms") or 0)
        if start_ms <= 0:
            raise ValueError("Missing session start.")
        end_ms = int(finished_at_ms) if finished_at_ms else _now_ms()
        total_ms = max(0, end_ms - start_ms)
        prof["participation_end_ms"] = end_ms
        prof["total_participation_ms"] = total_ms
        _put(_pk(session_id), _sk("PROFILE"), prof)
        return {"session_id": session_id, "total_participation_ms": total_ms}

    def log_total_task_time(session_id: str, bucket: str, elapsed_ms: int) -> Dict[str, Any]:
        key_pk, key_sk = _pk(session_id), _sk("TASK_TIME")
        cur = _get(key_pk, key_sk) or {"buckets": dict(DEFAULT_BUCKETS)}
        try:
            inc = int(elapsed_ms)
        except Exception:
            inc = 0
        inc = max(0, min(inc, _ATTENTION_MAX_INC_MS))

        buckets = cur.get("buckets") or {}
        if bucket not in buckets:
            return {"session_id": session_id, "ignored_bucket": bucket}

        buckets[bucket] = int(buckets.get(bucket, 0)) + inc
        cur["buckets"] = buckets
        cur["ts"] = _now_ms()
        _put(key_pk, key_sk, cur)
        return {"session_id": session_id, "bucket": bucket, "total_ms": buckets[bucket]}

    def log_reading_comprehension_details(session_id: str, event: Dict[str, Any]) -> Dict[str, Any]:
        passage_id = str(event.get("passage_id") or "")
        status = str(event.get("status") or "active")
        page_name = str(event.get("page_name") or "unknown")
        start_time = int(event.get("start_time") or 0)
        try:
            duration_ms = int(event.get("duration_ms") or 0)
        except Exception:
            duration_ms = 0
        duration_ms = max(0, min(duration_ms, _RC_MAX_SEG_MS))
        server_ts = _now_ms()

        events = RC_EVENTS[session_id]
        has_active_before = any(ev.get("passage_id") == passage_id and ev.get("status") == "active" for ev in events)

        if status == "blur" and not has_active_before and page_name == "unknown" and duration_ms <= _RC_SPURIOUS_BLUR_MAX_MS:
            return {"session_id": session_id, "start_time": start_time, "status": status, "passage_id": passage_id,
                    "page_name": page_name, "duration_ms": duration_ms, "server_ts": server_ts, "suppressed": True}

        if status == "active" and not has_active_before:
            for i in range(len(events) - 1, -1, -1):
                ev = events[i]
                if ev.get("passage_id") == passage_id:
                    if ev.get("status") == "blur" and (ev.get("page_name") or "unknown") == "unknown" and int(ev.get("duration_ms") or 0) <= _RC_SPURIOUS_BLUR_MAX_MS:
                        events.pop(i)
                    break

        if duration_ms < _RC_MIN_SEG_MS:
            return {"session_id": session_id, "start_time": start_time, "status": status, "passage_id": passage_id,
                    "page_name": page_name, "duration_ms": duration_ms, "server_ts": server_ts, "suppressed": True}

        if events:
            prev = events[-1]
            if prev.get("passage_id") == passage_id and prev.get("status") == status and (prev.get("page_name") or "unknown") == page_name:
                prev_end = int(prev.get("start_time", 0)) + int(prev.get("duration_ms", 0))
                gap = max(0, start_time - prev_end)
                if gap <= _RC_MERGE_GAP_MS:
                    prev["duration_ms"] = min(int(prev["duration_ms"]) + duration_ms + gap, _RC_MAX_SEG_MS)
                    prev["server_ts"] = server_ts
                    from_time = f"{prev['start_time']:013d}"  # keep same key if you also persist elsewhere
                    return prev

        rec = {"session_id": session_id, "start_time": start_time, "status": status, "passage_id": passage_id,
               "page_name": page_name, "duration_ms": duration_ms, "server_ts": server_ts}
        RC_EVENTS[session_id].append(rec)
        return rec

# =====================================================================
# AURORA (MySQL) BACKEND  — NEW
# =====================================================================
elif STORAGE_BACKEND == "aurora":
    # SQLAlchemy models + session
    from sqlalchemy import select
    from sqlalchemy.exc import IntegrityError
    from backend.database import SessionLocal, init_db
    from backend.models import (
        Session as DBSession,
        Demographics as DBDemographics,
        Assignment as DBAssignment,
        MCQSubmission as DBMCQSubmission,
        PostTaskFeedback as DBPostTaskFeedback,
        VocabFinal as DBVocabFinal,
        RCEvent as DBRCEvent,
        AttentionLog as DBAttentionLog,
        BucketNameEnum,
        FinalCheck as DBFinalCheck,
    )

    # initialize tables if needed
    init_db()

    # Small in-process for vocab "progress only"
    VOCAB_PROGRESS: Dict[str, Dict[str, Any]] = defaultdict(dict)

    def _db():
        return SessionLocal()

    def start_session(session_id: str, source: str | None = None) -> None:
        db = _db()
        try:
            exists = db.get(DBSession, session_id)
            if not exists:
                db.add(DBSession(id=session_id, source=source, consent=True))
                db.commit()
        finally:
            db.close()

    def session_exists(session_id: str) -> bool:
        db = _db()
        try:
            return db.get(DBSession, session_id) is not None
        finally:
            db.close()

    def save_demographics(session_id: str, payload: Dict[str, Any], recaptcha_verification: str | None = None) -> None:
        db = _db()
        try:
            sess = db.get(DBSession, session_id)
            if not sess:
                raise ValueError("Session not found.")
            row = db.get(DBDemographics, session_id)
            if not row:
                row = DBDemographics(session_id=session_id)
                db.add(row)
            # payload is already normalized/typed by pydantic in main.py
            row.prolific_id = payload.get("prolific_id")
            row.age = payload.get("age")
            row.gender = payload.get("gender")
            row.citizenship = payload.get("citizenship")
            row.ethnicity = payload.get("ethnicity")
            row.education = payload.get("education")
            row.first_language = payload.get("first_language")
            row.extras = payload.get("extras") or {}
            if recaptcha_verification in ("yes", "no"):
                row.recaptcha_verification = recaptcha_verification
            row.server_ts = row.server_ts or None  # default handled by model
            db.commit()
        finally:
            db.close()

    def mark_recaptcha_result(session_id: str, endpoint: str, ok: bool) -> None:
        # Optional: you can store these flags somewhere if you like.
        # Not strictly needed by the rest of the app.
        return

    def set_assignment(session_id: str, passage_ids: List[str]) -> None:
        db = _db()
        try:
            sess = db.get(DBSession, session_id)
            if not sess:
                raise ValueError("Session not found.")
            row = db.get(DBAssignment, session_id)
            if not row:
                row = DBAssignment(session_id=session_id, passage_ids=list(passage_ids), sources={})
                db.add(row)
            else:
                row.passage_ids = list(passage_ids)
            db.commit()
        finally:
            db.close()

    def get_assignment(session_id: str) -> List[str] | None:
        db = _db()
        try:
            row = db.get(DBAssignment, session_id)
            return (row.passage_ids if row else None)
        finally:
            db.close()

    def set_source_assignment(session_id: str, mapping: Dict[str, str]) -> None:
        db = _db()
        try:
            row = db.get(DBAssignment, session_id)
            if not row:
                # If randomize called fresh, set both
                row = DBAssignment(session_id=session_id, passage_ids=[], sources=dict(mapping))
                db.add(row)
            else:
                row.sources = dict(mapping)
            db.commit()
        finally:
            db.close()

    def get_source_for(session_id: str, passage_id: str) -> Optional[str]:
        db = _db()
        try:
            row = db.get(DBAssignment, session_id)
            if not row:
                return None
            srcs = row.sources or {}
            return srcs.get(passage_id)
        finally:
            db.close()

    def save_mcq_submission(session_id: str, passage_id: str, passage_uid: str, source: str,
                            per_question: List[Dict[str, Any]], score: int, meta: Dict[str, Any]) -> None:
        db = _db()
        try:
            exists_stmt = select(DBMCQSubmission).where(
                DBMCQSubmission.session_id == session_id, DBMCQSubmission.passage_id == passage_id
            )
            existing = db.execute(exists_stmt).scalar_one_or_none()
            if existing:
                existing.passage_uid = passage_uid
                existing.source = source
                existing.per_question = per_question
                existing.score = score
                existing.time_on_questions_ms = (meta or {}).get("time_on_questions_ms")
                existing.back_to_passage_clicks = int((meta or {}).get("back_to_passage_clicks") or 0)
            else:
                row = DBMCQSubmission(
                    session_id=session_id,
                    passage_id=passage_id,
                    passage_uid=passage_uid,
                    source=source,
                    per_question=per_question,
                    score=score,
                    time_on_questions_ms=(meta or {}).get("time_on_questions_ms"),
                    back_to_passage_clicks=int((meta or {}).get("back_to_passage_clicks") or 0),
                )
                db.add(row)
            db.commit()
        finally:
            db.close()

    def get_mcq_submission(session_id: str, passage_id: str) -> Optional[Dict[str, Any]]:
        db = _db()
        try:
            stmt = select(DBMCQSubmission).where(
                DBMCQSubmission.session_id == session_id, DBMCQSubmission.passage_id == passage_id
            )
            row = db.execute(stmt).scalar_one_or_none()
            if not row:
                return None
            return {
                "passage_uid": row.passage_uid,
                "source": row.source,
                "per_question": row.per_question,
                "score": row.score,
                "meta": {
                    "time_on_questions_ms": row.time_on_questions_ms,
                    "back_to_passage_clicks": row.back_to_passage_clicks,
                },
                "ts": int(row.created_at.timestamp() * 1000) if row.created_at else _now_ms(),
            }
        finally:
            db.close()

    def save_posttask_feedback(session_id: str, passage_uid: str, ratings: Dict[str, int]) -> None:
        db = _db()
        try:
            stmt = select(DBPostTaskFeedback).where(
                DBPostTaskFeedback.session_id == session_id,
                DBPostTaskFeedback.passage_uid == passage_uid
            )
            row = db.execute(stmt).scalar_one_or_none()
            if row:
                merged = dict(row.ratings or {})
                merged.update(ratings or {})
                row.ratings = merged
            else:
                db.add(DBPostTaskFeedback(session_id=session_id, passage_uid=passage_uid, ratings=ratings or {}))
            db.commit()
        finally:
            db.close()

    def init_vocab(session_id: str, size: int) -> None:
        VOCAB_PROGRESS[session_id] = {"index": 0, "size": size}

    def advance_vocab(session_id: str, item_id: str, is_word: bool, rt_ms: int | None, is_correct: bool) -> None:
        prog = VOCAB_PROGRESS[session_id]
        prog["index"] = int(prog.get("index", 0)) + 1

    def get_vocab_progress(session_id: str) -> Dict[str, Any]:
        return VOCAB_PROGRESS.get(session_id, {"index": 0, "size": 0})

    def save_vocab_final(session_id: str, trials: List[Dict[str, Any]]) -> None:
        db = _db()
        try:
            row = db.get(DBVocabFinal, session_id)
            if row:
                row.trials = trials or []
            else:
                db.add(DBVocabFinal(session_id=session_id, trials=trials or []))
            db.commit()
        finally:
            db.close()

    def final_check(session_id: str, data: Dict[str, Any], recaptcha_verification: str | None = None) -> None:
        db = _db()
        try:
            sess = db.get(DBSession, session_id)
            if not sess:
                raise ValueError("Session not found.")
            row = db.get(DBFinalCheck, session_id)
            payload = {
                "used_ai_tools": data.get("used_ai_tools"),
                "tools": list(data.get("tools") or []),
                "other_tool": (data.get("other_tool") or "").strip(),
            }
            if row:
                row.payload = payload
                if recaptcha_verification in ("yes", "no"):
                    row.recaptcha_verification = recaptcha_verification
            else:
                row = DBFinalCheck(
                    session_id=session_id,
                    payload=payload,
                    recaptcha_verification=(recaptcha_verification if recaptcha_verification in ("yes", "no") else None),
                )
                db.add(row)
            db.commit()
        finally:
            db.close()

    def log_total_participation_time(session_id: str, finished_at_ms: Optional[int] = None) -> Dict[str, Any]:
        db = _db()
        try:
            sess = db.get(DBSession, session_id)
            if not sess:
                raise ValueError("Session not found.")
            start_ms = int(sess.created_at.timestamp() * 1000) if sess.created_at else 0
            if start_ms <= 0:
                raise ValueError("Missing session start.")
            end_ms = int(finished_at_ms) if finished_at_ms else _now_ms()
            total_ms = max(0, end_ms - start_ms)
            sess.participation_end_ms = end_ms
            sess.total_participation_ms = total_ms
            db.commit()
            return {"session_id": session_id, "total_participation_ms": total_ms}
        finally:
            db.close()

    def log_total_task_time(session_id: str, bucket: str, elapsed_ms: int) -> Dict[str, Any]:
        db = _db()
        try:
            # validate bucket against enum
            if bucket not in {b.value for b in BucketNameEnum}:
                return {"session_id": session_id, "ignored_bucket": bucket}
            try:
                inc = int(elapsed_ms)
            except Exception:
                inc = 0
            inc = max(0, min(inc, _ATTENTION_MAX_INC_MS))

            stmt = select(DBAttentionLog).where(
                DBAttentionLog.session_id == session_id, DBAttentionLog.bucket == BucketNameEnum(bucket)
            )
            row = db.execute(stmt).scalar_one_or_none()
            if row:
                row.total_ms = int(row.total_ms or 0) + inc
            else:
                row = DBAttentionLog(session_id=session_id, bucket=BucketNameEnum(bucket), total_ms=inc)
                db.add(row)
            db.commit()
            return {"session_id": session_id, "bucket": bucket, "total_ms": row.total_ms}
        finally:
            db.close()

    def log_reading_comprehension_details(session_id: str, event: Dict[str, Any]) -> Dict[str, Any]:
        # NOTE: We only persist accepted segments; debounce/merge logic is typically handled in-memory.
        # For Aurora, we’ll accept the segment and write a row directly (no merge here).
        db = _db()
        try:
            sess = db.get(DBSession, session_id)
            if not sess:
                raise ValueError("Session not found.")
            # clamp duration
            try:
                duration_ms = int(event.get("duration_ms") or 0)
            except Exception:
                duration_ms = 0
            duration_ms = max(0, min(duration_ms, _RC_MAX_SEG_MS))
            rec = DBRCEvent(
                session_id=session_id,
                passage_id=str(event.get("passage_id") or ""),
                page_name=str(event.get("page_name") or "unknown"),
                status=str(event.get("status") or "active"),
                start_time=int(event.get("start_time") or 0),
                duration_ms=duration_ms,
            )
            db.add(rec)
            db.commit()
            return {"session_id": session_id, "start_time": rec.start_time,
                    "status": rec.status, "server_ts": int(rec.server_ts.timestamp() * 1000)}
        finally:
            db.close()

# =====================================================================
# Unsupported
# =====================================================================
else:
    raise ValueError(f"Unsupported STORAGE_BACKEND: {STORAGE_BACKEND}")
