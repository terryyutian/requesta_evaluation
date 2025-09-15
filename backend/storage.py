"""
Storage layer with in-memory default and optional DynamoDB backend.
Set STORAGE_BACKEND=dynamodb to enable AWS.

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
- init_vocab(session_id, size)
- advance_vocab(session_id, item_id, is_word, rt_ms)
- get_vocab_progress(session_id)
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

USE_DDB = os.getenv("STORAGE_BACKEND", "").lower() == "dynamodb"

if not USE_DDB:
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

    # session_id -> {index, answers: [{item_id,is_word,rt_ms,ts}], size}
    VOCAB_PROGRESS: Dict[str, Dict[str, Any]] = defaultdict(dict)

    # Per-session attention buckets
    TASK_TIME: DefaultDict[str, Dict[str, int]] = defaultdict(lambda: dict(DEFAULT_BUCKETS))

    # RC detailed events (in-memory list; used for blur suppression & also OK for export)
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
        DEMOGRAPHICS[session_id] = rec

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
        passage_uid: str,          # unique, e.g., 'anthropology_1_2'
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

    # --- Vocabulary task ---

    def init_vocab(session_id: str, size: int) -> None:
        VOCAB_PROGRESS[session_id] = {"index": 0, "answers": [], "size": size}

    def advance_vocab(session_id: str, item_id: str, is_word: bool, rt_ms: int | None) -> None:
        prog = VOCAB_PROGRESS[session_id]
        prog.setdefault("answers", []).append(
            {"item_id": item_id, "is_word": is_word, "rt_ms": rt_ms, "ts": time.time()}
        )
        prog["index"] = int(prog.get("index", 0)) + 1

    def get_vocab_progress(session_id: str) -> Dict[str, Any]:
        return VOCAB_PROGRESS.get(session_id, {"index": 0, "answers": [], "size": 0})

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

else:
    # ==========================================================
    # DynamoDB backend
    # ==========================================================
    import boto3
    from boto3.dynamodb.conditions import Key
    from decimal import Decimal

    # Local cache only for “fast” membership checks during one process lifetime.
    # NOTE: across restarts, rely on DDB; consider changing main.py to use
    # storage.session_exists(session_id) instead of checking SESSIONS directly.
    SESSIONS: Dict[str, Dict[str, Any]] = {}

    # For RC suppression/merge logic (kept in-memory), while accepted events also go to DDB:
    RC_EVENTS: DefaultDict[str, List[Dict[str, Any]]] = defaultdict(list)

    _REGION = os.getenv("AWS_REGION", "us-east-1")
    _DDB_ENDPOINT = os.getenv("DDB_ENDPOINT")  # optional (e.g., local)
    _TABLE_NAME = os.getenv("DDB_TABLE", "study_data")

    _ddb = boto3.resource("dynamodb", region_name=_REGION, endpoint_url=_DDB_ENDPOINT)
    _table = _ddb.Table(_TABLE_NAME)

    def _pk(session_id: str) -> str:
        return f"SESSION#{session_id}"

    def _sk(kind: str, suffix: str | None = None) -> str:
        return f"{kind}#{suffix}" if suffix else kind

    def _to_decimal(obj):
        if isinstance(obj, float):
            return Decimal(str(obj))
        if isinstance(obj, dict):
            return {k: _to_decimal(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [_to_decimal(v) for v in obj]
        return obj

    def _from_decimal(obj):
        if isinstance(obj, Decimal):
            as_float = float(obj)
            return int(as_float) if as_float.is_integer() else as_float
        if isinstance(obj, list):
            return [_from_decimal(v) for v in obj]
        if isinstance(obj, dict):
            return {k: _from_decimal(v) for k, v in obj.items()}
        return obj

    # --- Session & demographics ---

    def start_session(session_id: str, source: str | None = None) -> None:
        SESSIONS[session_id] = {"created_at": time.time(), "source": source, "consent": True}
        item = {
            "pk": _pk(session_id),
            "sk": _sk("PROFILE"),
            "created_at_ms": _now_ms(),
            "source": source,
            "consent": True,
        }
        _table.put_item(Item=_to_decimal(item))

    def save_demographics(
        session_id: str,
        payload: Dict[str, Any],
        recaptcha_verification: str | None = None,
    ) -> None:
        rec = dict(payload)
        if recaptcha_verification in ("yes", "no"):
            rec["recaptcha_verification"] = recaptcha_verification
        item = {
            "pk": _pk(session_id),
            "sk": _sk("DEMOGRAPHICS"),
            "payload": _to_decimal(rec),
            "server_ts": _now_ms(),
        }
        _table.put_item(Item=item)

    def mark_recaptcha_result(session_id: str, endpoint: str, ok: bool) -> None:
        # Update cached session too
        sess = SESSIONS.setdefault(session_id, {})
        sess[f"recaptcha_{endpoint}"] = "yes" if ok else "no"
        sess["recaptcha_ts"] = _now_ms()
        # Persist on PROFILE row
        _table.update_item(
            Key={"pk": _pk(session_id), "sk": _sk("PROFILE")},
            UpdateExpression="SET #f = :val, recaptcha_ts = :ts",
            ExpressionAttributeNames={"#f": f"recaptcha_{endpoint}"},
            ExpressionAttributeValues={":val": "yes" if ok else "no", ":ts": _now_ms()},
        )

    # --- Assignment helpers ---

    def set_assignment(session_id: str, passage_ids: List[str]) -> None:
        _table.update_item(
            Key={"pk": _pk(session_id), "sk": _sk("ASSIGNMENT")},
            UpdateExpression="SET passage_ids = :p, server_ts = :ts",
            ExpressionAttributeValues={":p": passage_ids, ":ts": _now_ms()},
        )

    def get_assignment(session_id: str) -> List[str] | None:
        resp = _table.get_item(Key={"pk": _pk(session_id), "sk": _sk("ASSIGNMENT")})
        return resp.get("Item", {}).get("passage_ids")

    def set_source_assignment(session_id: str, mapping: Dict[str, str]) -> None:
        _table.update_item(
            Key={"pk": _pk(session_id), "sk": _sk("ASSIGNMENT")},
            UpdateExpression="SET sources = :s, server_ts = :ts",
            ExpressionAttributeValues={":s": mapping, ":ts": _now_ms()},
        )

    def get_source_for(session_id: str, passage_id: str) -> Optional[str]:
        resp = _table.get_item(Key={"pk": _pk(session_id), "sk": _sk("ASSIGNMENT")})
        m = resp.get("Item", {}).get("sources") or {}
        return m.get(passage_id)

    # --- RC data persistence ---

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
            "pk": _pk(session_id),
            "sk": _sk("MCQ", passage_id),
            "passage_uid": passage_uid,
            "source": source,
            "per_question": _to_decimal(per_question),
            "score": score,
            "meta": _to_decimal(meta),
            "ts": _now_ms(),
        }
        _table.put_item(Item=item)

    def get_mcq_submission(session_id: str, passage_id: str) -> Optional[Dict[str, Any]]:
        resp = _table.get_item(Key={"pk": _pk(session_id), "sk": _sk("MCQ", passage_id)})
        item = resp.get("Item")
        return _from_decimal(item) if item else None

    def save_posttask_feedback(session_id: str, passage_uid: str, ratings: Dict[str, int]) -> None:
        # Merge with any existing ratings
        key = {"pk": _pk(session_id), "sk": _sk("POSTTASK", passage_uid)}
        existing = _table.get_item(Key=key).get("Item", {})
        merged = dict(existing.get("ratings") or {})
        merged.update(ratings)
        _table.put_item(Item={"pk": key["pk"], "sk": key["sk"], "ratings": merged, "ts": _now_ms()})

    # --- Vocabulary task ---

    def init_vocab(session_id: str, size: int) -> None:
        item = {
            "pk": _pk(session_id),
            "sk": _sk("VOCAB"),
            "index": 0,
            "size": size,
            "answers": [],
            "ts": _now_ms(),
        }
        _table.put_item(Item=item)

    def advance_vocab(session_id: str, item_id: str, is_word: bool, rt_ms: int | None) -> None:
        ans = [{"item_id": item_id, "is_word": bool(is_word), "rt_ms": rt_ms, "ts": _now_ms()}]
        _table.update_item(
            Key={"pk": _pk(session_id), "sk": _sk("VOCAB")},
            UpdateExpression="""
                SET #idx = if_not_exists(#idx, :zero) + :one,
                    #ans = list_append(if_not_exists(#ans, :empty), :new),
                    ts = :ts
            """,
            ExpressionAttributeNames={"#idx": "index", "#ans": "answers"},
            ExpressionAttributeValues={
                ":zero": 0, ":one": 1, ":empty": [], ":new": _to_decimal(ans), ":ts": _now_ms()
            },
        )

    def get_vocab_progress(session_id: str) -> Dict[str, Any]:
        resp = _table.get_item(Key={"pk": _pk(session_id), "sk": _sk("VOCAB")})
        item = resp.get("Item", {"index": 0, "answers": [], "size": 0})
        return _from_decimal(item)

    # --- Final check ---

    def final_check(session_id: str, data: Dict[str, Any], recaptcha_verification: str | None = None) -> None:
        rec = {
            "used_ai_tools": data.get("used_ai_tools"),
            "tools": list(data.get("tools") or []),
            "other_tool": (data.get("other_tool") or "").strip(),
            "server_ts": _now_ms(),
        }
        if recaptcha_verification in ("yes", "no"):
            rec["recaptcha_verification"] = recaptcha_verification
        _table.update_item(
            Key={"pk": _pk(session_id), "sk": _sk("PROFILE")},
            UpdateExpression="SET final_check = :fc",
            ExpressionAttributeValues={":fc": _to_decimal(rec)},
        )

    # --- Time logging ---

    def log_total_participation_time(session_id: str, finished_at_ms: Optional[int] = None) -> Dict[str, Any]:
        resp = _table.get_item(Key={"pk": _pk(session_id), "sk": _sk("PROFILE")})
        item = resp.get("Item")
        if not item:
            raise ValueError("Session not found.")
        start_ms = int(item.get("created_at_ms") or 0)
        if start_ms <= 0:
            raise ValueError("Missing session start.")
        end_ms = int(finished_at_ms) if finished_at_ms else _now_ms()
        total_ms = max(0, end_ms - start_ms)
        _table.update_item(
            Key={"pk": _pk(session_id), "sk": _sk("PROFILE")},
            UpdateExpression="SET participation_end_ms = :end, total_participation_ms = :tot",
            ExpressionAttributeValues={":end": end_ms, ":tot": total_ms},
        )
        return {"session_id": session_id, "total_participation_ms": total_ms}

    def log_total_task_time(session_id: str, bucket: str, elapsed_ms: int) -> Dict[str, Any]:
        key = {"pk": _pk(session_id), "sk": _sk("TASK_TIME")}
        resp = _table.get_item(Key=key)
        cur = resp.get("Item", {"pk": key["pk"], "sk": key["sk"], "buckets": dict(DEFAULT_BUCKETS)})

        # Harden: clamp and cap per-call increments
        try:
            inc = int(elapsed_ms)
        except Exception:
            inc = 0
        inc = max(0, inc)
        inc = min(inc, _ATTENTION_MAX_INC_MS)

        if bucket not in cur["buckets"]:
            # Unknown buckets are ignored (compatible with client)
            return {"session_id": session_id, "ignored_bucket": bucket}

        cur["buckets"][bucket] = int(cur["buckets"].get(bucket, 0)) + inc
        cur["ts"] = _now_ms()
        _table.put_item(Item=cur)
        return {"session_id": session_id, "bucket": bucket, "total_ms": cur["buckets"][bucket]}

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
                    # Optional: keep DDB parity by updating the existing row
                    _table.update_item(
                        Key={"pk": _pk(session_id), "sk": _sk("RC", f"{prev['start_time']:013d}")},
                        UpdateExpression="SET duration_ms = :d, server_ts = :ts",
                        ExpressionAttributeValues={":d": int(prev["duration_ms"]), ":ts": server_ts},
                    )
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

        ddb_item = {
            "pk": _pk(session_id),
            "sk": _sk("RC", f"{start_time:013d}"),  # sortable
            **rec,
        }
        _table.put_item(Item=_to_decimal(ddb_item))
        return rec

# -----------------------------
# (Robust) existence check
# -----------------------------

def session_exists(session_id: str) -> bool:
    """Robust existence check. In-memory True if present; in DDB mode, query DynamoDB."""
    if session_id in SESSIONS:
        return True
    if not USE_DDB:
        return False
    resp = _table.get_item(Key={"pk": f"SESSION#{session_id}", "sk": "PROFILE"})
    found = "Item" in resp
    if found:  # warm the cache
        SESSIONS.setdefault(session_id, {})
    return found
