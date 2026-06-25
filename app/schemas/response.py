from pydantic import BaseModel
from typing import Any
from typing import Dict


class MessageResponse(BaseModel):
    message: str


class ErrorResponse(BaseModel):
    error: str


class AskResponse(BaseModel):
    question: str
    responses: Dict[str, Any]
    final: str


class SmartResponse(BaseModel):
    question: str
    selected_model: str
    answer: str


class AgentResponse(BaseModel):
    version: str
    session_id: str
    question: str
    route: str
    history_count: int
    answer: str