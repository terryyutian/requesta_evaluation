from fastapi import FastAPI, HTTPException, Depends, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import math
import time

from .schemas import (
    SessionStartRequest, SessionStartResponse, DemographicsPayload, RandomizeResponse,
    Passage, QuestionsResponse, SubmitMCQPayload, MCQSubmitResult, PostTaskFeedbackPayload,
   VocabNextResponse, VocabItem, VocabAnswerPayload, AttentionLogPayload, RCEventPayload, ParticipationEndRequest
)
from .security import new_session_id
from .randomizer import random_two_passages, maybe_shuffle_choices
from .data import PASSAGES, QUESTIONS, VOCAB
from .helper import normalize_demographics
from . import storage

app = FastAPI(title="Study Data Collection API", version="0.1.0")

# CORS: allow your front-end origin(s)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

    # Validate + coerce into your Pydantic model (keeps type safety)
    model = DemographicsPayload(**normalized)

    storage.save_demographics(session_id, model.model_dump())
    return {"ok": True}

# --- Random assignment ---
@app.post("/api/randomize", response_model=RandomizeResponse)
def randomize(session_id: str):
    if session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")
    assigned = random_two_passages()
    storage.set_assignment(session_id, assigned)
    return RandomizeResponse(passage_ids=assigned)

# --- Passages & questions ---
@app.get("/api/passage/{passage_id}", response_model=Passage)
def get_passage(passage_id: str, session_id: str):
    if session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")
    p = PASSAGES.get(passage_id)
    if not p:
        raise HTTPException(status_code=404, detail="Passage not found.")
    return Passage(**p)

@app.get("/api/questions/{passage_id}", response_model=QuestionsResponse)
def get_questions(passage_id: str, session_id: str):
    if session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")
    qs = QUESTIONS.get(passage_id)
    if not qs or len(qs) < 5:
        raise HTTPException(status_code=404, detail="No questions for passage.")
    #shuffled = maybe_shuffle_choices(qs, seed=None)
    return QuestionsResponse(
        passage_id=passage_id,
        questions=qs
    )

# --- Submit MCQs ---
@app.post("/api/submit_mcq", response_model=MCQSubmitResult)
def submit_mcq(payload: SubmitMCQPayload):
    if payload.session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")
    questions = QUESTIONS.get(payload.passage_id, [])
    qmap = {q["id"]: q for q in questions}
    per = []
    score = 0
    for qid, ans in payload.answers.items():
        correct = qmap[qid]["correct_choice_id"]
        ok = ans == correct
        if ok:
            score += 1
        per.append({
            "question_id": qid,
            "user_choice_id": ans,
            "correct_choice_id": correct,
            "is_correct": ok
        })
    storage.save_mcq_submission(
        session_id=payload.session_id,
        passage_id=payload.passage_id,
        per_question=per,
        score=score,
        meta={
            "time_on_questions_ms": payload.time_on_questions_ms,
            "back_to_passage_clicks": payload.back_to_passage_clicks
        }
    )
    return MCQSubmitResult(passage_id=payload.passage_id, per_question=per, score=score)

# --- Post-task feedback ---
@app.post("/api/posttask")
def posttask_feedback(payload: PostTaskFeedbackPayload):
    if payload.session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")
    storage.save_posttask_feedback(payload.session_id, payload.ratings)
    return {"ok": True}

# Provide data for post-task view (answers + correctness + passage)
@app.get("/api/posttask_data/{passage_id}")
def posttask_data(passage_id: str, session_id: str):
    if session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")
    passage = PASSAGES.get(passage_id)
    mcq = storage.MCQ_RESPONSES.get(session_id, {}).get(passage_id)
    if not passage or not mcq:
        raise HTTPException(status_code=404, detail="Not ready.")
    # Expand questions prompts for display
    qmap = {q["id"]: q for q in QUESTIONS[passage_id]}
    details = []
    for row in mcq["per_question"]:
        q = qmap[row["question_id"]]
        details.append({
            "question_id": row["question_id"],
            "prompt": q["prompt"],
            "choices": q["choices"],
            "user_choice_id": row["user_choice_id"],
            "correct_choice_id": row["correct_choice_id"],
            "is_correct": row["is_correct"],
        })
    return {
        "passage": passage,
        "questions": details,
        "score": mcq["score"]
    }

# --- Vocab test ---
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
    return VocabNextResponse(
        done=False,
        remaining=max(0, min(size, len(VOCAB)) - idx),
        item=VocabItem(id=item["id"], token=item["token"])
    )

@app.post("/api/vocab/answer")
def vocab_answer(payload: VocabAnswerPayload):
    if payload.session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")
    storage.advance_vocab(payload.session_id, payload.item_id, payload.is_word, payload.rt_ms)
    return {"ok": True}


@app.post("/api/final_check")
def submit_final_check(payload: Dict[str, Any] = Body(...), session_id: str = ""):
    if not session_id or session_id not in storage.SESSIONS:
        raise HTTPException(status_code=404, detail="Session not found.")
    storage.final_check(session_id, payload)
    return {"ok": True}

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
    return {
        "ok": True,
        "start_time": rec["start_time"],
        "server_ts": rec["server_ts"],
    }