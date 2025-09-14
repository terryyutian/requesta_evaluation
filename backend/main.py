# backend/main.py
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from typing import Any, Dict, List, Optional
import hashlib
import random

from schemas import (
    SessionStartRequest,
    SessionStartResponse,
    DemographicsPayload,
    RandomizeResponse,
    Passage,
    QuestionsResponse,
    SubmitMCQPayload,
    MCQSubmitResult,
    PostTaskFeedbackPayload,
    VocabNextResponse,
    VocabItem,
    VocabAnswerPayload,
    AttentionLogPayload,
    RCEventPayload,
    ParticipationEndRequest,
)
from security import new_session_id
from data import PASSAGES, QUESTIONS, VOCAB
from helper import normalize_demographics
import storage


app = FastAPI(title="Study Data Collection API", version="0.2.0")

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Helpers for deterministic assignment ---

def _sha_seed(text: str) -> int:
    return int(hashlib.sha256(text.encode("utf-8")).hexdigest(), 16) % (2**31)


def _has_two_sources(pkey: str) -> bool:
    try:
        q = QUESTIONS[pkey]["questions"]
        return (
            "baseline" in q
            and "requesta" in q
            and isinstance(q["baseline"], list)
            and isinstance(q["requesta"], list)
            and len(q["baseline"]) >= 6
            and len(q["requesta"]) >= 6
        )
    except Exception:
        return False


def _random_three_passages(seed: int | None = None) -> List[str]:
    """
    Deterministically pick 3 distinct passage KEYS (e.g., 'p1', 'p2', ...) that exist
    in PASSAGES and QUESTIONS, preferring those that have both sources available.
    """
    rng = random.Random(seed)

    preferred = [pid for pid in PASSAGES.keys() if pid in QUESTIONS and _has_two_sources(pid)]
    fallback = [pid for pid in PASSAGES.keys() if pid in QUESTIONS]

    pool = preferred if len(preferred) >= 3 else fallback
    if len(pool) < 3:
        raise HTTPException(status_code=500, detail="Not enough passages available.")

    rng.shuffle(pool)
    return pool[:3]


def _assign_sources_for_three(passage_ids: List[str], seed: int | None = None) -> Dict[str, str]:
    """
    Produce a deterministic 2:1 split across the three passages.
    Returns mapping: {passage_key: 'baseline'|'requesta'}.
    """
    if len(passage_ids) != 3:
        raise ValueError("Need exactly 3 passage ids")
    rng = random.Random(seed)
    majority = rng.choice(["baseline", "requesta"])
    minority = "requesta" if majority == "baseline" else "baseline"
    ids = passage_ids[:]
    rng.shuffle(ids)
    return {ids[0]: majority, ids[1]: majority, ids[2]: minority}


# --- Health ---

@app.get("/api/health")
def health():
    return {"ok": True}


# --- Session & consent ---

@app.post("/api/session/start", response_model=SessionStartResponse)
def session_start(req: SessionStartRequest):
    if not req.consent:
        raise HTTPException(status_code=400, detail="Consent required.")
    sid = new_session_id()
    storage.start_session(sid, source=req.source)
    return SessionStartResponse(session_id=sid)


# --- Demographics ---

@app.post("/api/demographics")
def submit_demographics(payload: Dict[str, Any] = Body(...), session_id: str = ""):
    if session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")
    normalized = normalize_demographics(payload)
    model = DemographicsPayload(**normalized)
    storage.save_demographics(session_id, model.model_dump())
    return {"ok": True}


# --- Random assignment (3 passages + 2:1 source split, deterministic) ---

@app.post("/api/randomize", response_model=RandomizeResponse)
def randomize(session_id: str):
    if session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")

    base_seed = _sha_seed(session_id)
    passages = _random_three_passages(seed=base_seed)
    storage.set_assignment(session_id, passages)

    # derive a different seed for sources so passage choice doesn't fully determine split
    source_seed = (base_seed * 31 + 7) % (2**31)
    source_map = _assign_sources_for_three(passages, seed=source_seed)
    storage.set_source_assignment(session_id, source_map)

    return RandomizeResponse(passage_ids=passages)


# --- Passages ---

@app.get("/api/passage/{passage_id}", response_model=Passage)
def get_passage(passage_id: str, session_id: str):
    if session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")
    p = PASSAGES.get(passage_id)
    if not p:
        raise HTTPException(status_code=404, detail="Passage not found.")
    return Passage(**p)


# --- Questions (serve the chosen source with 6 questions) ---

@app.get("/api/questions/{passage_id}", response_model=QuestionsResponse)
def get_questions(passage_id: str, session_id: str):
    if session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")
    src = storage.get_source_for(session_id, passage_id)
    if not src:
        raise HTTPException(status_code=400, detail="Source not assigned for this passage.")

    pq = QUESTIONS.get(passage_id)
    if not pq:
        raise HTTPException(status_code=404, detail="No questions for passage.")
    qset = pq.get("questions", {}).get(src) or []
    if len(qset) < 6:
        raise HTTPException(status_code=500, detail="Insufficient questions for assigned source.")

    # Map your new structure → existing schema (id ← question_id)
    mapped = []
    for q in qset:
        mapped.append(
            {
                "id": q["question_id"],
                "prompt": q["prompt"],
                "choices": q["choices"],
                "correct_choice_id": q["correct_choice_id"],
            }
        )
    return QuestionsResponse(passage_id=passage_id, questions=mapped)


# --- Submit MCQs (store passage_uid & unique question_id) ---

@app.post("/api/submit_mcq", response_model=MCQSubmitResult)
def submit_mcq(payload: SubmitMCQPayload):
    if payload.session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")
    src = storage.get_source_for(payload.session_id, payload.passage_id)
    if not src:
        raise HTTPException(status_code=400, detail="Source not assigned for this passage.")

    pq = QUESTIONS.get(payload.passage_id)
    if not pq:
        raise HTTPException(status_code=404, detail="No question data for passage.")
    qset = pq.get("questions", {}).get(src) or []
    qmap = {q["question_id"]: q for q in qset}

    per: List[Dict[str, Any]] = []
    score = 0
    for qid, ans in (payload.answers or {}).items():
        if qid not in qmap:
            # Ignore unknown keys silently (robust to stale client state)
            continue
        correct = qmap[qid]["correct_choice_id"]
        ok = (ans == correct)
        if ok:
            score += 1
        per.append(
            {
                "question_id": qid,
                "user_choice_id": ans,
                "correct_choice_id": correct,
                "is_correct": ok,
            }
        )

    passage_uid = (PASSAGES.get(payload.passage_id) or {}).get("id") or payload.passage_id
    storage.save_mcq_submission(
        session_id=payload.session_id,
        passage_id=payload.passage_id,
        passage_uid=passage_uid,
        source=src,
        per_question=per,
        score=score,
        meta={
            "time_on_questions_ms": payload.time_on_questions_ms,
            "back_to_passage_clicks": payload.back_to_passage_clicks,
        },
    )
    return MCQSubmitResult(passage_id=payload.passage_id, per_question=per, score=score)


# --- Post-task feedback (store under passage_uid) ---

@app.post("/api/posttask")
def posttask_feedback(payload: PostTaskFeedbackPayload):
    if payload.session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")
    p = PASSAGES.get(payload.passage_id)
    if not p:
        raise HTTPException(status_code=404, detail="Passage not found.")
    storage.save_posttask_feedback(payload.session_id, p["id"], payload.ratings or {})
    return {"ok": True}


# Provide data for post-task view (exclude QX*)

@app.get("/api/posttask_data/{passage_id}")
def posttask_data(passage_id: str, session_id: str):
    if session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")

    passage = PASSAGES.get(passage_id)
    mcq = storage.MCQ_RESPONSES.get(session_id, {}).get(passage_id)
    if not passage or not mcq:
        raise HTTPException(status_code=404, detail="Not ready.")

    src = mcq.get("source")
    pq = QUESTIONS.get(passage_id) or {}
    qset = pq.get("questions", {}).get(src) or []
    qmap = {q["question_id"]: q for q in qset}

    details: List[Dict[str, Any]] = []
    for row in mcq["per_question"]:
        qid = row["question_id"]
        # Skip attention checks in post-task: any id starting with "QX" (case-insensitive)
        if str(qid).upper().startswith("QX"):
            continue
        q = qmap.get(qid)
        if not q:
            continue
        details.append(
            {
                "question_id": qid,
                "prompt": q["prompt"],
                "choices": q["choices"],
                "user_choice_id": row["user_choice_id"],
                "correct_choice_id": row["correct_choice_id"],
                "is_correct": row["is_correct"],
            }
        )

    return {"passage": passage, "questions": details, "score": mcq["score"]}


# --- Vocabulary task ---

@app.post("/api/vocab/start")
def vocab_start(session_id: str):
    if session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")
    storage.init_vocab(session_id, size=len(VOCAB))
    return {"ok": True, "size": len(VOCAB)}


@app.get("/api/vocab/next", response_model=VocabNextResponse)
def vocab_next(session_id: str):
    prog = storage.get_vocab_progress(session_id)
    idx = prog.get("index", 0)
    size = prog.get("size", len(VOCAB))
    if idx >= size or idx >= len(VOCAB):
        return VocabNextResponse(done=True, remaining=0, item=None)
    item = VOCAB[idx]

    # Ensure ID exists before returning
    iid = item.get("id") or f"v{idx}"
    item["id"] = iid  # persist for later lookups

    remaining = max(0, min(size, len(VOCAB)) - idx)  # includes current item
    return VocabNextResponse(done=False, remaining=remaining, item=VocabItem(id=iid, token=item["token"]))


@app.post("/api/vocab/answer")
def vocab_answer(payload: VocabAnswerPayload):
    if payload.session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")

    # Look up truth label for this item_id
    truth: Optional[bool] = None
    for it in VOCAB:
        if it.get("id") == payload.item_id:
            truth = it.get("is_word")
            break
    if truth is None:
        raise HTTPException(status_code=400, detail="Unknown vocabulary item.")

    # Persist the response
    storage.advance_vocab(payload.session_id, payload.item_id, payload.is_word, payload.rt_ms)

    # Return immediate correctness for the HUD
    return {"ok": True, "correct": bool(payload.is_word == truth)}


# --- Final check ---

@app.post("/api/final_check")
def submit_final_check(payload: Dict[str, Any] = Body(...), session_id: str = ""):
    if not session_id or session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")
    storage.final_check(session_id, payload)
    return {"ok": True}


# --- Logging endpoints ---

@app.post("/api/log/participation_end")
def log_participation_end(payload: ParticipationEndRequest):
    if payload.session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")
    try:
        res = storage.log_total_participation_time(payload.session_id, payload.finished_at_ms)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return res


@app.post("/api/log/attention")
def log_attention(payload: AttentionLogPayload):
    if payload.session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")
    try:
        res = storage.log_total_task_time(payload.session_id, payload.bucket, payload.elapsed_ms)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return res


@app.post("/api/log/rc_event")
def log_rc_event(payload: RCEventPayload):
    # Validate session
    if payload.session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")

    # Persist the RC event (no event_seq)
    try:
        rec = storage.log_reading_comprehension_details(
            payload.session_id,
            {
                "start_time": payload.start_time,
                "status": payload.status,
                "passage_id": payload.passage_id,
                "page_name": payload.page_name or "unknown",
                "duration_ms": payload.duration_ms or 0,
            },
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Return a simple ACK (optionally echo back timestamps for debugging)
    return {"ok": True, "start_time": rec["start_time"], "server_ts": rec["server_ts"]}
