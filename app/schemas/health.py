from pydantic import BaseModel
from typing import List


class HealthResponse(BaseModel):
    status: str
    version: str
    providers: List[str]
    features: List[str]