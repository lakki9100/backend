from fastapi import APIRouter
from models.chat_model import ChatRequest
from services.secret_service import SecretService
from services.gemini_service import GeminiService

router = APIRouter()
secret_service = SecretService()
gemini = GeminiService(secret_service)

@router.post("/chat")
def chat(request: ChatRequest):
    return {"reply": gemini.chat(request.place_name, request.message)}