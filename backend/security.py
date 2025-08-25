import uuid

def new_session_id() -> str:
    return str(uuid.uuid4())
