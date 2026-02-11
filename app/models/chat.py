from pydantic import BaseModel
from typing import List, Optional

class ChatRequest(BaseModel):
    query: str
    session_id: str = "default"
    model: str = "gpt-4-turbo-preview"

class Source(BaseModel):
    text: str
    filename: Optional[str]
    chunk_id: Optional[int]

class ChatResponse(BaseModel):
    answer: str
    sources: List[Source]
    session_id: str
