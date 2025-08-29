"""
Minimal placeholder storage.

By default uses in-memory dicts. You can swap these out for SQLite/CSV/S3, etc.
"""

from __future__ import annotations
from typing import Dict, Any, List, DefaultDict, Tuple
from collections import defaultdict
import time
import threading

# --- In-memory stores (replace with DB as needed) ---
SESSIONS: Dict[str, Dict[str, Any]] = {}  # session_id -> info
DEMOGRAPHICS: Dict[str, Dict[str, Any]] = {}
ASSIGNMENTS: Dict[str, List[str]] = {}    # session_id -> [pid1, pid2]
MCQ_RESPONSES: Dict[str, Dict[str, Any]] = defaultdict(dict)  # session_id -> passage_id -> details
POSTTASK: Dict[str, Dict[str, int]] = defaultdict(dict)       # session_id -> {question_id: +1/-1}
VOCAB_PROGRESS: Dict[str, Dict[str, Any]] = defaultdict(dict) # session_id -> {index, answers}
# Per-session log and sequence counter
EVENT_LOG: DefaultDict[str, List[Dict[str, Any]]] = defaultdict(list)
SESSION_EVENT_SEQ: DefaultDict[str, int] = defaultdict(int)

# Track last ACTIVE by (session_id, page_instance_id)
LAST_ACTIVE: Dict[Tuple[str, str], Dict[str, Any]] = {}



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
    print(f"Vocab progress for {session_id}: {VOCAB_PROGRESS.get(session_id)}")
    return VOCAB_PROGRESS.get(session_id, {"index": 0, "answers": [], "size": 0})
    #TODO: Save to a DB


_lock = threading.Lock()

def _now_ms() -> int:
  return int(time.time() * 1000)

def log_event(evt: Dict[str, Any]) -> Dict[str, Any]:
  """
  Expects payload from client with:
    session_id, seq (optional), event_type ('active'|'blur'),
    page_name, start_time (client ms), page_instance_id, meta
  Returns stored record with finalized seq and server_ts.
  When event_type == 'blur', computes duration_ms for the preceding 'active'
  with the same (session_id, page_instance_id).
  """
  session_id = str(evt.get("session_id") or "")
  if not session_id:
    raise ValueError("session_id required")

  event_type = str(evt.get("event_type") or "")
  if event_type not in ("active", "blur"):
    raise ValueError("event_type must be 'active' or 'blur'")

  page_name = str(evt.get("page_name") or "unknown")
  page_instance_id = str(evt.get("page_instance_id") or "")
  if not page_instance_id:
    raise ValueError("page_instance_id required")

  start_time = int(evt.get("start_time") or 0)

  meta = evt.get("meta") or {}
  # Enforce RC requirements
  if page_name in ("passage", "questions"):
    if "passage_index" not in meta or "passage_id" not in meta:
      raise ValueError("RC pages require meta.passage_index and meta.passage_id")
    if page_name == "questions":
      if "question_index" not in meta or "question_id" not in meta:
        raise ValueError("questions page requires meta.question_index and meta.question_id")

  client_seq = int(evt.get("seq") or 0)
  with _lock:
    last = SESSION_EVENT_SEQ[session_id]
    seq_final = max(last + 1, client_seq)
    SESSION_EVENT_SEQ[session_id] = seq_final

  record: Dict[str, Any] = {
    "session_id": session_id,
    "seq": seq_final,
    "event_type": event_type,
    "page_name": page_name,
    "meta": meta,
    "start_time": start_time,
    "server_ts": _now_ms(),
    "page_instance_id": page_instance_id,
  }

  # Compute duration on blur based on matching ACTIVE
  if event_type == "blur":
    key = (session_id, page_instance_id)
    prev = LAST_ACTIVE.get(key)
    if prev:
      # prefer client clocks; fall back to server if needed
      start = int(prev.get("start_time") or 0)
      end = start_time if start_time else record["server_ts"]
      start = start if start else int(prev.get("server_ts") or record["server_ts"])
      duration = max(0, int(end) - int(start))
      record["duration_ms"] = duration
      # this active is now closed
      LAST_ACTIVE.pop(key, None)
    else:
      # no matching active found; still store the event
      record["duration_ms"] = None

  elif event_type == "active":
    # overwrite/replace last active for this page instance
    key = (session_id, page_instance_id)
    LAST_ACTIVE[key] = record

  EVENT_LOG[session_id].append(record)
  return record

def get_events(session_id: str) -> List[Dict[str, Any]]:
  return list(EVENT_LOG.get(session_id, []))


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

