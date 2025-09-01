from typing import List, Optional, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict

class SessionStartRequest(BaseModel):
    source: Optional[str] = None
    consent: bool = True

class SessionStartResponse(BaseModel):
    session_id: str

class DemographicsPayload(BaseModel):
    # Keep accepting extra fields (Q1–Q12) while explicitly modeling citizenship
    model_config = ConfigDict(extra='allow')

    prolific_id: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    citizenship: Optional[List[str]] = None
    ethnicity: Optional[str] = None
    education: Optional[str] = None
    first_language: Optional[str] = None
    # Optional catch-all if you still want it
    extras: Dict[str, Any] = Field(default_factory=dict)

class RandomizeResponse(BaseModel):
    passage_ids: List[str]  # exactly two in this template

class Passage(BaseModel):
    id: str
    title: str
    text: str

class Choice(BaseModel):
    id: str
    text: str

class Question(BaseModel):
    id: str
    prompt: str
    choices: List[Choice]
    correct_choice_id: str

class QuestionsResponse(BaseModel):
    passage_id: str
    questions: List[Question]

class SubmitMCQPayload(BaseModel):
    session_id: str
    passage_id: str
    answers: Dict[str, str]  # {question_id: choice_id}
    time_on_questions_ms: Optional[int] = None
    back_to_passage_clicks: Optional[int] = 0

class MCQSubmitResult(BaseModel):
    passage_id: str
    per_question: List[Dict[str, Any]]  # qid, user_choice_id, correct_choice_id, is_correct
    score: int

class PostTaskFeedbackPayload(BaseModel):
    session_id: str
    passage_id: str
    ratings: Dict[str, int]  # {question_id: +1/-1}

class VocabItem(BaseModel):
    id: str
    token: str

class VocabNextResponse(BaseModel):
    done: bool
    remaining: int
    item: Optional[VocabItem] = None

class VocabAnswerPayload(BaseModel):
    session_id: str
    item_id: str
    is_word: bool
    rt_ms: Optional[int] = None


class ParticipationEndRequest(BaseModel):
    session_id: str
    finished_at_ms: Optional[int] = None  # optional; server will use now() if missing

BucketName = Literal[
    "consent","demographic","reading_instruction",
    "reading_task1","survey_task1",
    "reading_task2","survey_task2",
    "vocabulary"
]

class AttentionLogPayload(BaseModel):
    session_id: str
    bucket: BucketName
    elapsed_ms: int  # focused time delta to add

class RCEventPayload(BaseModel):
    session_id: str
    passage_id: str
    page_name: str    # e.g., "p1", "p1q3"; use "unknown" for blur events
    status: Literal["active","blur"]
    start_time: int   # client ms epoch (Date.now())
    duration_ms: int  # duration of this segment
