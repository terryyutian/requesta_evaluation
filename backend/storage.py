"""
Minimal placeholder storage.

By default uses in-memory dicts. You can swap these out for SQLite/CSV/S3, etc.
"""

from __future__ import annotations
from typing import Dict, Any, List, Optional, DefaultDict  
from collections import defaultdict
import time
import threading  

def _now_ms() -> int:  # add this helper
    return int(time.time() * 1000)

# --- In-memory stores (replace with DB as needed) ---
SESSIONS: Dict[str, Dict[str, Any]] = {}  # session_id -> info
DEMOGRAPHICS: Dict[str, Dict[str, Any]] = {}
ASSIGNMENTS: Dict[str, List[str]] = {}    # session_id -> [pid1, pid2]
MCQ_RESPONSES: Dict[str, Dict[str, Any]] = defaultdict(dict)  # session_id -> passage_id -> details
POSTTASK: Dict[str, Dict[str, int]] = defaultdict(dict)       # session_id -> {question_id: +1/-1}
VOCAB_PROGRESS: Dict[str, Dict[str, Any]] = defaultdict(dict) # session_id -> {index, answers}



def start_session(session_id: str, source: str | None = None) -> None:
    SESSIONS[session_id] = {"created_at": time.time(), "source": source, "consent": True}

def save_demographics(session_id: str, payload: Dict[str, Any]) -> None:
    print(f"Saving demographics for {session_id}: {payload}")
    DEMOGRAPHICS[session_id] = payload
    #TODO: Save to a DB 

def set_assignment(session_id: str, passage_ids: List[str]) -> None:
    ASSIGNMENTS[session_id] = passage_ids

def get_assignment(session_id: str) -> List[str] | None:
    return ASSIGNMENTS.get(session_id)

def save_mcq_submission(session_id: str, passage_id: str, per_question: List[Dict[str, Any]], score: int, meta: Dict[str, Any]) -> None:
    print(f"Saving MCQ submission for {session_id}, passage {passage_id}: score {score}, details: {per_question}")
    MCQ_RESPONSES[session_id][passage_id] = {"per_question": per_question, "score": score, "meta": meta, "ts": time.time()}
    #TODO: Save to a DB

def save_posttask_feedback(session_id: str, ratings: Dict[str, int]) -> None:
    print(f"Saving post-task feedback for {session_id}: {ratings}")
    POSTTASK[session_id].update(ratings)
    #TODO: Save to a DB

def init_vocab(session_id: str, size: int) -> None:
    VOCAB_PROGRESS[session_id] = {"index": 0, "answers": [], "size": size}

def advance_vocab(session_id: str, item_id: str, is_word: bool, rt_ms: int | None) -> None:
    prog = VOCAB_PROGRESS[session_id]
    prog["answers"].append({"item_id": item_id, "is_word": is_word, "rt_ms": rt_ms, "ts": time.time()})
    prog["index"] += 1

def get_vocab_progress(session_id: str) -> Dict[str, Any]:
    #print(f"Vocab progress for {session_id}: {VOCAB_PROGRESS.get(session_id)}")
    return VOCAB_PROGRESS.get(session_id, {"index": 0, "answers": [], "size": 0})
    #TODO: Save to a DB


def final_check(session_id: str, data: Dict[str, Any]) -> None:
    """
    Persist the final self-report about external tool usage.
    Expected data:
      {
        "used_ai_tools": "Yes" | "No" | "Prefer not to say",
        "tools": List[str],            # may include "Other"
        "other_tool": str              # optional free text when "Other" picked
      }
    """
    rec = {
      "used_ai_tools": data.get("used_ai_tools"),
      "tools": list(data.get("tools") or []),
      "other_tool": (data.get("other_tool") or "").strip(),
      "server_ts": int(time.time() * 1000),
    }
    sess = SESSIONS.setdefault(session_id, {})
    sess["final_check"] = rec


# --- logging ---
# --- add below existing globals ---

# Per-session attention buckets
TASK_TIME: DefaultDict[str, Dict[str, int]] = defaultdict(lambda: {
    "consent":0, "demographic":0, "reading_instruction":0,
    "reading_task1":0, "survey_task1":0,
    "reading_task2":0, "survey_task2":0,
    "vocabulary":0
})

# RC detailed events + per-session event sequence
RC_EVENTS: DefaultDict[str, List[Dict[str, Any]]] = defaultdict(list)


def log_total_participation_time(session_id: str, finished_at_ms: Optional[int] = None) -> Dict[str, Any]:
    """
    Compute and persist total participation time (ms) from session created_at.
    """
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
    print(f"Session {session_id} total participation time: {total_ms} ms")
    return {"session_id": session_id, "total_participation_ms": total_ms}


def log_total_task_time(session_id: str, bucket: str, elapsed_ms: int) -> Dict[str, Any]:
    """
    Add focused elapsed_ms to one bucket for this session.
    """
    if session_id not in SESSIONS:
        raise ValueError("Session not found.")
    if bucket not in TASK_TIME[session_id]:
        # ignore unknown bucket names silently (keeps it robust)
        return {"session_id": session_id, "ignored_bucket": bucket}
    elapsed_ms = max(0, int(elapsed_ms))
    TASK_TIME[session_id][bucket] += elapsed_ms
    print(f"Session {session_id} +{elapsed_ms} ms to {bucket}, total now {TASK_TIME[session_id][bucket]} ms")
    return {"session_id": session_id, "bucket": bucket, "total_ms": TASK_TIME[session_id][bucket]}


# storage.py

def log_reading_comprehension_details(session_id: str, event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Append one RC event. We rely on start_time (client ms) for ordering.
    Suppress the initial spurious blur that sometimes fires before the first active.

    Rules:
      - If the first event for a given passage_id is a tiny 'blur' with page_name='unknown',
        drop it (do not store).
      - If we receive the first 'active' and the immediately-previous event for that
        passage_id is a tiny 'blur' with page_name='unknown', remove that blur retroactively.

    A "tiny" blur is <= SPURIOUS_BLUR_MAX_MS (tweak as needed).
    """
    if session_id not in SESSIONS:
        raise ValueError("Session not found.")

    SPURIOUS_BLUR_MAX_MS = 250  # adjust if you encounter legitimate short blurs

    passage_id = str(event.get("passage_id") or "")
    status = str(event.get("status") or "active")
    page_name = str(event.get("page_name") or "unknown")
    start_time = int(event.get("start_time") or 0)
    duration_ms = max(0, int(event.get("duration_ms") or 0))
    server_ts = int(time.time() * 1000)

    # Convenience handle to this session's events
    events = RC_EVENTS[session_id]

    # Did we already record an 'active' for this passage?
    has_active_before = any(
        ev.get("passage_id") == passage_id and ev.get("status") == "active"
        for ev in events
    )

    # 1) Drop a *leading* tiny blur for this passage (before any active)
    if (
        status == "blur"
        and not has_active_before
        and page_name == "unknown"
        and duration_ms <= SPURIOUS_BLUR_MAX_MS
    ):
        print(f"Session {session_id}: suppressed initial spurious blur for {passage_id} ({duration_ms} ms)")
        # Return a minimal record to keep call sites happy; nothing persisted.
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

    # 2) If this is the *first* active, and the immediately previous event for this passage
    #    is a tiny blur, remove that blur retroactively.
    if status == "active" and not has_active_before:
        # find the most recent event for this passage (if any)
        for i in range(len(events) - 1, -1, -1):
            ev = events[i]
            if ev.get("passage_id") == passage_id:
                if (
                    ev.get("status") == "blur"
                    and (ev.get("page_name") or "unknown") == "unknown"
                    and int(ev.get("duration_ms") or 0) <= SPURIOUS_BLUR_MAX_MS
                ):
                    removed = events.pop(i)
                    print(f"Session {session_id}: removed leading spurious blur before first active for {passage_id}: {removed}")
                break  # Only inspect the most recent entry for this passage

    # Store the (possibly cleaned) event
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
    print(f"Session {session_id} logged RC event: {rec}")
    return rec


# NOTE: We assume a single-process server (e.g., uvicorn workers=1).
# Sequence increments are safe without a lock in this setup because
# the function is synchronous and completes before yielding.
# If we scale beyond one process, move counters to a shared store
# (SQLite/Postgres/Redis) and use an atomic increment there.
