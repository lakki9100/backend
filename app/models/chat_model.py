from pydantic import BaseModel

class ChatRequest(BaseModel):
    place_name: str
    message: str
