import google.generativeai as genai
from services.secret_service import SecretService

class GeminiService:
    def __init__(self, secret_service: SecretService):
        self.api_key = secret_service.get("GEMINI_API_KEY")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

    def chat(self, place_name: str, message: str) -> str:
        response = self.model.generate_content(
            f"You are a helpful assistant answering questions about {place_name}. User asked: {message}"
        )
        return response.text
