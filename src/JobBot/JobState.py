from langgraph.graph import MessagesState
from pydantic import BaseModel
from typing_extensions import TypedDict

class JobState(TypedDict, total=False):
    source: str
    description: str
    cover_letter: str
    resume: str
    job_feedback: str | None