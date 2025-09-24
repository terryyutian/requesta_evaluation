# backend/models.py
from sqlalchemy import (
    Column, Integer, BigInteger, String, Boolean, ForeignKey, JSON, DateTime,
    Enum, UniqueConstraint
)
from sqlalchemy.orm import declarative_base, relationship
import datetime
import enum

Base = declarative_base()

class BucketNameEnum(enum.Enum):
    consent = "consent"
    demographic = "demographic"
    reading_instruction = "reading_instruction"
    reading_task1 = "reading_task1"
    survey_task1 = "survey_task1"
    reading_task2 = "reading_task2"
    survey_task2 = "survey_task2"
    reading_task3 = "reading_task3"
    survey_task3 = "survey_task3"
    vocabulary = "vocabulary"

class Session(Base):
    __tablename__ = "sessions"

    id = Column(String(64), primary_key=True)
    source = Column(String(128), nullable=True)
    consent = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Optional metrics we store during logs:
    participation_end_ms = Column(BigInteger, nullable=True)
    total_participation_ms = Column(Integer, nullable=True)

    demographics = relationship("Demographics", uselist=False, back_populates="session")
    mcq_submissions = relationship("MCQSubmission", back_populates="session")
    vocab_submission = relationship("VocabFinal", uselist=False, back_populates="session")
    rc_events = relationship("RCEvent", back_populates="session")
    attention_logs = relationship("AttentionLog", back_populates="session")
    posttask_feedback = relationship("PostTaskFeedback", back_populates="session")
    assignment = relationship("Assignment", uselist=False, back_populates="session")
    final_check = relationship("FinalCheck", uselist=False, back_populates="session")

class Demographics(Base):
    __tablename__ = "demographics"

    session_id = Column(String(64), ForeignKey("sessions.id"), primary_key=True)
    prolific_id = Column(String(128), nullable=True)
    age = Column(Integer, nullable=True)
    gender = Column(String(64), nullable=True)
    citizenship = Column(JSON)
    ethnicity = Column(String(128), nullable=True)
    education = Column(String(128), nullable=True)
    first_language = Column(String(128), nullable=True)
    extras = Column(JSON)
    recaptcha_verification = Column(String(16), nullable=True)
    server_ts = Column(DateTime, default=datetime.datetime.utcnow)

    session = relationship("Session", back_populates="demographics")

class Assignment(Base):
    __tablename__ = "assignments"

    session_id = Column(String(64), ForeignKey("sessions.id"), primary_key=True)
    passage_ids = Column(JSON)        # list[str]
    sources = Column(JSON)            # {passage_key: "baseline"|"requesta"}
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    session = relationship("Session", back_populates="assignment")

class MCQSubmission(Base):
    __tablename__ = "mcq_submissions"
    __table_args__ = (UniqueConstraint('session_id', 'passage_id', name='uniq_mcq_session_passage'),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(64), ForeignKey("sessions.id"))
    passage_id = Column(String(32))
    passage_uid = Column(String(128))
    source = Column(String(32))
    per_question = Column(JSON)
    score = Column(Integer)
    time_on_questions_ms = Column(Integer, nullable=True)
    back_to_passage_clicks = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    session = relationship("Session", back_populates="mcq_submissions")

class PostTaskFeedback(Base):
    __tablename__ = "posttask_feedback"
    __table_args__ = (UniqueConstraint('session_id', 'passage_uid', name='uniq_posttask'),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(64), ForeignKey("sessions.id"))
    passage_uid = Column(String(128))
    ratings = Column(JSON)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    session = relationship("Session", back_populates="posttask_feedback")

class VocabFinal(Base):
    __tablename__ = "vocab_final"

    session_id = Column(String(64), ForeignKey("sessions.id"), primary_key=True)
    trials = Column(JSON)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    session = relationship("Session", back_populates="vocab_submission")

class RCEvent(Base):
    __tablename__ = "rc_events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(64), ForeignKey("sessions.id"))
    passage_id = Column(String(64))
    page_name = Column(String(128))
    status = Column(Enum("active", "blur"))
    start_time = Column(Integer)  # client epoch ms
    duration_ms = Column(Integer)
    server_ts = Column(DateTime, default=datetime.datetime.utcnow)

    session = relationship("Session", back_populates="rc_events")

class AttentionLog(Base):
    __tablename__ = "attention_logs"
    __table_args__ = (UniqueConstraint('session_id', 'bucket', name='uniq_attention'),)

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(64), ForeignKey("sessions.id"))
    bucket = Column(Enum(BucketNameEnum), nullable=False)
    total_ms = Column(Integer, default=0)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    session = relationship("Session", back_populates="attention_logs")

class FinalCheck(Base):
    __tablename__ = "final_checks"

    session_id = Column(String(64), ForeignKey("sessions.id"), primary_key=True)
    payload = Column(JSON)                 # the dict you post (tools, etc.)
    recaptcha_verification = Column(String(16), nullable=True)
    server_ts = Column(DateTime, default=datetime.datetime.utcnow)

    session = relationship("Session", back_populates="final_check")
