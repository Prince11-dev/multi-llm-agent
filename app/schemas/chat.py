from pydantic import BaseModel
from typing import Optional


class AskRequest(BaseModel):
    question: str


class SmartRequest(BaseModel):
    question: str


class AgentRequest(BaseModel):
    question: str
    session_id: Optional[str] = "default"


class SearchRequest(BaseModel):
    question: str


class CompareRequest(BaseModel):
    question: str