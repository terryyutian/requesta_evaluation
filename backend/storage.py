"""
Storage layer with in-memory default and optional SQLite backend.

Set STORAGE_BACKEND=sqlite to enable SQLite.

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

# Optional SQLite backend
USE_SQLITE = os.getenv("STORAGE_BACKEND", "").lower() == "sqlite"
print(f"Storage backend: {'SQLite' if USE_SQLITE else 'in-memory (dev only)'}")
_SQLITE_PATH = os.getenv("SQLITE_PATH", "study_data.db")

# -----------------------------
# Common helpers / defaults
# -----------------------------

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

# -----------------------------
# Backend selector
# -----------------------------

if not USE_SQLITE:
    # ==========================================================
    # In-memory backend (also used for testing)
    # ==========================================================

    # session_id -> info
    SESSIONS: Dict[str, Dict[str, Any]] = {}

    # session_id -> demographics payload
    DEMOGRAPHICS: Dict[str, Dict[str, Any]] = {}

    # session_id -> [passage_key1, passage_key2, passage_key3]
    ASSIGNMENTS: Dict[str, List[str]] = {}

    # session_id -> {passage_key: "baseline"|"requesta"}
    ASSIGNED_SOURCES: DefaultDict[str, Dict[str, str]] = defaultdict(dict)

    # MCQ responses
    MCQ_RESPONSES: Dict[str, Dict[str, Any]] = defaultdict(dict)

    # session_id -> passage_uid -> {question_id: +1/-1}
    POSTTASK: Dict[str, Dict[str, Dict[str, int]]] = defaultdict(dict)

    # --- Vocabulary (progress only; final payload is saved via save_vocab_final) ---
    # session_id -> {index, size}
    VOCAB_PROGRESS: Dict[str, Dict[str, Any]] = defaultdict(dict)

    # Final vocab one-row store (for parity with persisted backends)
    VOCAB_FINAL: Dict[str, Dict[str, Any]] = defaultdict(dict)

    # Per-session attention buckets
    TASK_TIME: DefaultDict[str, Dict[str, int]] = defaultdict(lambda: dict(DEFAULT_BUCKETS))

    # RC detailed events (in-memory list; used for blur suppression/merge & export)
    RC_EVENTS: DefaultDict[str, List[Dict[str, Any]]] = defaultdict(list)

    # --- Session & demographics ---

    def start_session(session_id: str, source: str | None = None) -> None:
        SESSIONS[session_id] = {"created_at": time.time(), "source": source, "consent": True}

    def save_demographics(
        session_id: str,
        payload: Dict[str, Any],
        recaptcha_verification: str | None = None,
    ) -> None:
        rec = dict(payload)
        if recaptcha_verification in ("yes", "no"):
            rec["recaptcha_verification"] = recaptcha_verification
        DEMOGRAPHICS[session_id] = {"payload": rec, "server_ts": _now_ms()}

    def mark_recaptcha_result(session_id: str, endpoint: str, ok: bool) -> None:
        sess = SESSIONS.setdefault(session_id, {})
        sess[f"recaptcha_{endpoint}"] = "yes" if ok else "no"
        sess["recaptcha_ts"] = _now_ms()

    # --- Assignment helpers ---

    def set_assignment(session_id: str, passage_ids: List[str]) -> None:
        ASSIGNMENTS[session_id] = passage_ids

    def get_assignment(session_id: str) -> List[str] | None:
        return ASSIGNMENTS.get(session_id)

    def set_source_assignment(session_id: str, mapping: Dict[str, str]) -> None:
        ASSIGNED_SOURCES[session_id] = dict(mapping)

    def get_source_for(session_id: str, passage_id: str) -> Optional[str]:
        return ASSIGNED_SOURCES.get(session_id, {}).get(passage_id)

    # --- RC data persistence ---

    def save_mcq_submission(
        session_id: str,
        passage_id: str,           # key like 'p7'
        passage_uid: str,          # e.g., 'anthropology_1_2'
        source: str,               # 'baseline' | 'requesta'
        per_question: List[Dict[str, Any]],
        score: int,
        meta: Dict[str, Any],
    ) -> None:
        MCQ_RESPONSES[session_id][passage_id] = {
            "passage_uid": passage_uid,
            "source": source,
            "per_question": per_question,
            "score": score,
            "meta": meta,
            "ts": time.time(),
        }

    def get_mcq_submission(session_id: str, passage_id: str) -> Optional[Dict[str, Any]]:
        """Return the graded submission dict or None."""
        return MCQ_RESPONSES.get(session_id, {}).get(passage_id)

    def save_posttask_feedback(session_id: str, passage_uid: str, ratings: Dict[str, int]) -> None:
        if passage_uid not in POSTTASK[session_id]:
            POSTTASK[session_id][passage_uid] = {}
        POSTTASK[session_id][passage_uid].update(ratings)

    # --- Vocabulary task (progress only) ---

    def init_vocab(session_id: str, size: int) -> None:
        VOCAB_PROGRESS[session_id] = {"index": 0, "size": size}

    def advance_vocab(session_id: str, item_id: str, is_word: bool, rt_ms: int | None, is_correct: bool) -> None:
        # We only advance the index; we do NOT persist per-click answers
        prog = VOCAB_PROGRESS[session_id]
        prog["index"] = int(prog.get("index", 0)) + 1

    def get_vocab_progress(session_id: str) -> Dict[str, Any]:
        return VOCAB_PROGRESS.get(session_id, {"index": 0, "size": 0})

    def save_vocab_final(session_id: str, trials: List[Dict[str, Any]]) -> None:
        # Single final row per session (kept in-memory in this backend)
        VOCAB_FINAL[session_id] = {"trials": trials, "ts": _now_ms()}

    # --- Final check ---

    def final_check(
        session_id: str,
        data: Dict[str, Any],
        recaptcha_verification: str | None = None,
    ) -> None:
        rec = {
            "used_ai_tools": data.get("used_ai_tools"),
            "tools": list(data.get("tools") or []),
            "other_tool": (data.get("other_tool") or "").strip(),
            "server_ts": _now_ms(),
        }
        if recaptcha_verification in ("yes", "no"):
            rec["recaptcha_verification"] = recaptcha_verification
        sess = SESSIONS.setdefault(session_id, {})
        sess["final_check"] = rec

    # --- Time logging ---

    def log_total_participation_time(session_id: str, finished_at_ms: Optional[int] = None) -> Dict[str, Any]:
        sess = SESSIONS.get(session_id)
        if not sess:
            raise ValueError("Session not found.")
        start_s = float(sess.get("created_at") or 0.0)
        if start_s <= 0:
            raise ValueError("Missing session start.")
        end_ms = int(finished_at_ms) if finished_at_ms else _now_ms()
        total_ms = max(0, end_ms - int(start_s * 1000))
        sess["participation_end_ms"] = end_ms
        sess["total_participation_ms"] = total_ms
        return {"session_id": session_id, "total_participation_ms": total_ms}

    def log_total_task_time(session_id: str, bucket: str, elapsed_ms: int) -> Dict[str, Any]:
        if session_id not in SESSIONS:
            raise ValueError("Session not found.")
        if bucket not in TASK_TIME[session_id]:
            return {"session_id": session_id, "ignored_bucket": bucket}

        # Harden: clamp and cap per-call increments
        try:
            inc = int(elapsed_ms)
        except Exception:
            inc = 0
        inc = max(0, inc)
        inc = min(inc, _ATTENTION_MAX_INC_MS)

        TASK_TIME[session_id][bucket] += inc
        return {"session_id": session_id, "bucket": bucket, "total_ms": TASK_TIME[session_id][bucket]}

    def log_reading_comprehension_details(session_id: str, event: Dict[str, Any]) -> Dict[str, Any]:
        if session_id not in SESSIONS:
            raise ValueError("Session not found.")

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
        has_active_before = any(
            ev.get("passage_id") == passage_id and ev.get("status") == "active" for ev in events
        )

        # Suppress very first micro blur
        if (
            status == "blur"
            and not has_active_before
            and page_name == "unknown"
            and duration_ms <= _RC_SPURIOUS_BLUR_MAX_MS
        ):
            return {
                "session_id": session_id,
                "start_time": start_time,
                "status": status,
                "passage_id": passage_id,
                "page_name": page_name,
                "duration_ms": duration_ms,
                "server_ts": server_ts,
                "suppressed": True,
            }

        # If first ACTIVE arrives, retroactively drop last micro-blur
        if status == "active" and not has_active_before:
            for i in range(len(events) - 1, -1, -1):
                ev = events[i]
                if ev.get("passage_id") == passage_id:
                    if (
                        ev.get("status") == "blur"
                        and (ev.get("page_name") or "unknown") == "unknown"
                        and int(ev.get("duration_ms") or 0) <= _RC_SPURIOUS_BLUR_MAX_MS
                    ):
                        events.pop(i)
                    break

        # General micro-segment debounce
        if duration_ms < _RC_MIN_SEG_MS:
            return {
                "session_id": session_id,
                "start_time": start_time,
                "status": status,
                "passage_id": passage_id,
                "page_name": page_name,
                "duration_ms": duration_ms,
                "server_ts": server_ts,
                "suppressed": True,
            }

        # Merge with previous if identical state and adjacent
        if events:
            prev = events[-1]
            if (
                prev.get("passage_id") == passage_id
                and prev.get("status") == status
                and (prev.get("page_name") or "unknown") == page_name
            ):
                prev_end = int(prev.get("start_time", 0)) + int(prev.get("duration_ms", 0))
                gap = max(0, start_time - prev_end)
                if gap <= _RC_MERGE_GAP_MS:
                    prev["duration_ms"] = min(int(prev["duration_ms"]) + duration_ms + gap, _RC_MAX_SEG_MS)
                    prev["server_ts"] = server_ts
                    return prev

        # Otherwise, append a new record
        rec = {
            "session_id": session_id,
            "start_time": start_time,
            "status": status,
            "passage_id": passage_id,
            "page_name": page_name,
            "duration_ms": duration_ms,
            "server_ts": server_ts,
        }
        RC_EVENTS[session_id].append(rec)
        return rec

    # -----------------------------
    # (Robust) existence check
    # -----------------------------

    def session_exists(session_id: str) -> bool:
        return session_id in SESSIONS

else:
    # ==========================================================
    # SQLite backend (single kv table with pk/sk)
    # ==========================================================
    import sqlite3
    import threading

    # Small in-process cache for "fast" membership checks and RC merge logic
    SESSIONS: Dict[str, Dict[str, Any]] = {}
    RC_EVENTS: DefaultDict[str, List[Dict[str, Any]]] = defaultdict(list)

    _LOCK = threading.RLock()
    _conn = sqlite3.connect(_SQLITE_PATH, check_same_thread=False)
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

    # --- Session & demographics ---

    def start_session(session_id: str, source: str | None = None) -> None:
        SESSIONS[session_id] = {"created_at": time.time(), "source": source, "consent": True}
        profile = {
            "created_at_ms": _now_ms(),
            "source": source,
            "consent": True,
        }
        _put(_pk(session_id), _sk("PROFILE"), profile)

    def save_demographics(
        session_id: str,
        payload: Dict[str, Any],
        recaptcha_verification: str | None = None,
    ) -> None:
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

    # --- Assignment helpers ---

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

    # --- RC / MCQ data persistence ---

    def save_mcq_submission(
        session_id: str,
        passage_id: str,
        passage_uid: str,
        source: str,
        per_question: List[Dict[str, Any]],
        score: int,
        meta: Dict[str, Any],
    ) -> None:
        item = {
            "passage_uid": passage_uid,
            "source": source,
            "per_question": per_question,
            "score": score,
            "meta": meta,
            "ts": _now_ms(),
        }
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

    # --- Vocabulary task ---
    # NOTE: For "one-row final only", we do NOT persist per-click progress in SQLite.
    # We keep small progress (index/size) in-process to serve /api/vocab/next.

    VOCAB_PROGRESS: Dict[str, Dict[str, Any]] = defaultdict(dict)

    def init_vocab(session_id: str, size: int) -> None:
        VOCAB_PROGRESS[session_id] = {"index": 0, "size": size}

    def advance_vocab(session_id: str, item_id: str, is_word: bool, rt_ms: int | None, is_correct: bool) -> None:
        prog = VOCAB_PROGRESS[session_id]
        prog["index"] = int(prog.get("index", 0)) + 1

    def get_vocab_progress(session_id: str) -> Dict[str, Any]:
        return VOCAB_PROGRESS.get(session_id, {"index": 0, "size": 0})

    def save_vocab_final(session_id: str, trials: List[Dict[str, Any]]) -> None:
        # Exactly ONE row per session for vocabulary payload
        _put(_pk(session_id), _sk("VOCAB"), {"trials": trials, "ts": _now_ms()})

    # --- Final check ---

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

    # --- Time logging ---

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
        # clamp/cap increment
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

    # --- RC detailed events (with in-memory suppression/merge logic) ---

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
        has_active_before = any(
            ev.get("passage_id") == passage_id and ev.get("status") == "active" for ev in events
        )

        # First micro blur suppression
        if (
            status == "blur"
            and not has_active_before
            and page_name == "unknown"
            and duration_ms <= _RC_SPURIOUS_BLUR_MAX_MS
        ):
            return {
                "session_id": session_id,
                "start_time": start_time,
                "status": status,
                "passage_id": passage_id,
                "page_name": page_name,
                "duration_ms": duration_ms,
                "server_ts": server_ts,
                "suppressed": True,
            }

        # Drop prior micro-blur if first ACTIVE arrives
        if status == "active" and not has_active_before:
            for i in range(len(events) - 1, -1, -1):
                ev = events[i]
                if ev.get("passage_id") == passage_id:
                    if (
                        ev.get("status") == "blur"
                        and (ev.get("page_name") or "unknown") == "unknown"
                        and int(ev.get("duration_ms") or 0) <= _RC_SPURIOUS_BLUR_MAX_MS
                    ):
                        events.pop(i)
                    break

        # General micro-segment debounce
        if duration_ms < _RC_MIN_SEG_MS:
            return {
                "session_id": session_id,
                "start_time": start_time,
                "status": status,
                "passage_id": passage_id,
                "page_name": page_name,
                "duration_ms": duration_ms,
                "server_ts": server_ts,
                "suppressed": True,
            }

        # Merge with previous if identical state and adjacent
        if events:
            prev = events[-1]
            if (
                prev.get("passage_id") == passage_id
                and prev.get("status") == status
                and (prev.get("page_name") or "unknown") == page_name
            ):
                prev_end = int(prev.get("start_time", 0)) + int(prev.get("duration_ms", 0))
                gap = max(0, start_time - prev_end)
                if gap <= _RC_MERGE_GAP_MS:
                    prev["duration_ms"] = min(int(prev["duration_ms"]) + duration_ms + gap, _RC_MAX_SEG_MS)
                    prev["server_ts"] = server_ts
                    # Update existing RC row too
                    _put(_pk(session_id), _sk("RC", f"{prev['start_time']:013d}"), prev)
                    return prev

        # Append + write accepted event
        rec = {
            "session_id": session_id,
            "start_time": start_time,
            "status": status,
            "passage_id": passage_id,
            "page_name": page_name,
            "duration_ms": duration_ms,
            "server_ts": server_ts,
        }
        RC_EVENTS[session_id].append(rec)
        _put(_pk(session_id), _sk("RC", f"{start_time:013d}"), rec)
        return rec

    # -----------------------------
    # (Robust) existence check
    # -----------------------------

    def session_exists(session_id: str) -> bool:
        if session_id in SESSIONS:
            return True
        # query kv PROFILE
        pk = _pk(session_id)
        with _LOCK:
            cur = _conn.execute("SELECT 1 FROM kv WHERE pk=? AND sk='PROFILE' LIMIT 1", (pk,))
            found = cur.fetchone() is not None
        if found:
            SESSIONS.setdefault(session_id, {})
        return found
