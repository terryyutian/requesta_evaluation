"""
Minimal in-memory storage with logging utilities.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any, DefaultDict, Dict, List, Optional
import time


def _now_ms() -> int:
    return int(time.time() * 1000)


# --- In-memory stores (replace with DB as needed) ---

# session_id -> info
SESSIONS: Dict[str, Dict[str, Any]] = {}

# session_id -> demographics payload
DEMOGRAPHICS: Dict[str, Dict[str, Any]] = {}

# session_id -> [passage_key1, passage_key2, passage_key3]
ASSIGNMENTS: Dict[str, List[str]] = {}

# session_id -> {passage_key: "baseline"|"requesta"}
ASSIGNED_SOURCES: DefaultDict[str, Dict[str, str]] = defaultdict(dict)

# session_id -> passage_key -> details
# details: {
#   "passage_uid": str,
#   "source": str,
#   "per_question": [{question_id, user_choice_id, correct_choice_id, is_correct}],
#   "score": int,
#   "meta": {time_on_questions_ms, back_to_passage_clicks},
#   "ts": float
# }
MCQ_RESPONSES: Dict[str, Dict[str, Any]] = defaultdict(dict)

# session_id -> passage_uid -> {question_id: +1/-1}
POSTTASK: Dict[str, Dict[str, Dict[str, int]]] = defaultdict(dict)

# session_id -> {index, answers: [{item_id,is_word,rt_ms,ts}], size}
VOCAB_PROGRESS: Dict[str, Dict[str, Any]] = defaultdict(dict)

# Per-session attention buckets
TASK_TIME: DefaultDict[str, Dict[str, int]] = defaultdict(
    lambda: {
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
)

# RC detailed events
RC_EVENTS: DefaultDict[str, List[Dict[str, Any]]] = defaultdict(list)


# --- Session & demographics ---

def start_session(session_id: str, source: str | None = None) -> None:
    SESSIONS[session_id] = {"created_at": time.time(), "source": source, "consent": True}


def save_demographics(session_id: str, payload: Dict[str, Any]) -> None:
    DEMOGRAPHICS[session_id] = payload


# --- Assignment helpers ---

def set_assignment(session_id: str, passage_ids: List[str]) -> None:
    """Store the 3 selected passage KEYS for this session."""
    ASSIGNMENTS[session_id] = passage_ids


def get_assignment(session_id: str) -> List[str] | None:
    return ASSIGNMENTS.get(session_id)


def set_source_assignment(session_id: str, mapping: Dict[str, str]) -> None:
    """Store which source ('baseline'|'requesta') was chosen for each passage key."""
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


def save_posttask_feedback(session_id: str, passage_uid: str, ratings: Dict[str, int]) -> None:
    """
    Store ratings under the unique passage id to disambiguate across keys.
    """
    if passage_uid not in POSTTASK[session_id]:
        POSTTASK[session_id][passage_uid] = {}
    POSTTASK[session_id][passage_uid].update(ratings)


# --- Vocabulary task ---

def init_vocab(session_id: str, size: int) -> None:
    VOCAB_PROGRESS[session_id] = {"index": 0, "answers": [], "size": size}


def advance_vocab(session_id: str, item_id: str, is_word: bool, rt_ms: int | None) -> None:
    prog = VOCAB_PROGRESS[session_id]
    prog["answers"].append(
        {"item_id": item_id, "is_word": is_word, "rt_ms": rt_ms, "ts": time.time()}
    )
    prog["index"] += 1


def get_vocab_progress(session_id: str) -> Dict[str, Any]:
    return VOCAB_PROGRESS.get(session_id, {"index": 0, "answers": [], "size": 0})


# --- Final check ---

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
        "server_ts": _now_ms(),
    }
    sess = SESSIONS.setdefault(session_id, {})
    sess["final_check"] = rec


# --- Time logging ---

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
    return {"session_id": session_id, "total_participation_ms": total_ms}


def log_total_task_time(session_id: str, bucket: str, elapsed_ms: int) -> Dict[str, Any]:
    """
    Add focused elapsed_ms to one bucket for this session.
    Unknown buckets are ignored silently to keep client robust.
    """
    if session_id not in SESSIONS:
        raise ValueError("Session not found.")
    if bucket not in TASK_TIME[session_id]:
        return {"session_id": session_id, "ignored_bucket": bucket}
    elapsed_ms = max(0, int(elapsed_ms))
    TASK_TIME[session_id][bucket] += elapsed_ms
    return {"session_id": session_id, "bucket": bucket, "total_ms": TASK_TIME[session_id][bucket]}


def log_reading_comprehension_details(session_id: str, event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Append one RC event. We rely on start_time (client ms) for ordering.
    Suppress the initial spurious blur that sometimes fires before the first active.

    Rules:
      - If the first event for a given passage_id is a tiny 'blur' with page_name='unknown',
        drop it (do not store).
      - If we receive the first 'active' and the immediately-previous event for that
        passage_id is a tiny 'blur' with page_name='unknown', remove that blur retroactively.

    A "tiny" blur is <= SPURIOUS_BLUR_MAX_MS.
    """
    if session_id not in SESSIONS:
        raise ValueError("Session not found.")

    SPURIOUS_BLUR_MAX_MS = 250  # adjust if you encounter legitimate short blurs

    passage_id = str(event.get("passage_id") or "")
    status = str(event.get("status") or "active")
    page_name = str(event.get("page_name") or "unknown")
    start_time = int(event.get("start_time") or 0)
    duration_ms = max(0, int(event.get("duration_ms") or 0))
    server_ts = _now_ms()

    events = RC_EVENTS[session_id]

    # Did we already record an 'active' for this passage?
    has_active_before = any(
        ev.get("passage_id") == passage_id and ev.get("status") == "active" for ev in events
    )

    # 1) Drop a *leading* tiny blur for this passage (before any active)
    if (
        status == "blur"
        and not has_active_before
        and page_name == "unknown"
        and duration_ms <= SPURIOUS_BLUR_MAX_MS
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

    # 2) If this is the *first* active, and the immediately previous event for this passage
    #    is a tiny blur, remove that blur retroactively.
    if status == "active" and not has_active_before:
        for i in range(len(events) - 1, -1, -1):
            ev = events[i]
            if ev.get("passage_id") == passage_id:
                if (
                    ev.get("status") == "blur"
                    and (ev.get("page_name") or "unknown") == "unknown"
                    and int(ev.get("duration_ms") or 0) <= SPURIOUS_BLUR_MAX_MS
                ):
                    events.pop(i)
                break

    # Store the event
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
