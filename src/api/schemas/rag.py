from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"

class ChatResponse(BaseModel):
    answer: str
    context: list[str] = []

class UploadResponse(BaseModel):
    filename: str
    message: str
