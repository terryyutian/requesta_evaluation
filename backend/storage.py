"""
Minimal placeholder storage.

By default uses in-memory dicts. You can swap these out for SQLite/CSV/S3, etc.
"""

from __future__ import annotations
from typing import Dict, Any, List
from collections import defaultdict
import time

# --- In-memory stores (replace with DB as needed) ---
SESSIONS: Dict[str, Dict[str, Any]] = {}  # session_id -> info
DEMOGRAPHICS: Dict[str, Dict[str, Any]] = {}
ASSIGNMENTS: Dict[str, List[str]] = {}    # session_id -> [pid1, pid2]
MCQ_RESPONSES: Dict[str, Dict[str, Any]] = defaultdict(dict)  # session_id -> passage_id -> details
POSTTASK: Dict[str, Dict[str, int]] = defaultdict(dict)       # session_id -> {question_id: +1/-1}
VOCAB_PROGRESS: Dict[str, Dict[str, Any]] = defaultdict(dict) # session_id -> {index, answers}
EVENT_LOG: List[Dict[str, Any]] = []

def start_session(session_id: str, source: str | None = None) -> None:
    SESSIONS[session_id] = {"created_at": time.time(), "source": source, "consent": True}

def save_demographics(session_id: str, payload: Dict[str, Any]) -> None:
    DEMOGRAPHICS[session_id] = payload

def set_assignment(session_id: str, passage_ids: List[str]) -> None:
    ASSIGNMENTS[session_id] = passage_ids

def get_assignment(session_id: str) -> List[str] | None:
    return ASSIGNMENTS.get(session_id)

def save_mcq_submission(session_id: str, passage_id: str, per_question: List[Dict[str, Any]], score: int, meta: Dict[str, Any]) -> None:
    MCQ_RESPONSES[session_id][passage_id] = {"per_question": per_question, "score": score, "meta": meta, "ts": time.time()}

def save_posttask_feedback(session_id: str, ratings: Dict[str, int]) -> None:
    POSTTASK[session_id].update(ratings)

def init_vocab(session_id: str, size: int) -> None:
    VOCAB_PROGRESS[session_id] = {"index": 0, "answers": [], "size": size}

def advance_vocab(session_id: str, item_id: str, is_word: bool, rt_ms: int | None) -> None:
    prog = VOCAB_PROGRESS[session_id]
    prog["answers"].append({"item_id": item_id, "is_word": is_word, "rt_ms": rt_ms, "ts": time.time()})
    prog["index"] += 1

def get_vocab_progress(session_id: str) -> Dict[str, Any]:
    return VOCAB_PROGRESS.get(session_id, {"index": 0, "answers": [], "size": 0})

def log_event(session_id: str, event_type: str, meta: Dict[str, Any]) -> None:
    EVENT_LOG.append({"session_id": session_id, "event_type": event_type, "meta": meta, "ts": time.time()})
