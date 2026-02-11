from openai import OpenAI
from app.core.config import get_settings

settings = get_settings()

class EmbeddingService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def get_embedding(self, text: str, model: str = "text-embedding-ada-002") -> list[float]:
        text = text.replace("\n", " ")
        return self.client.embeddings.create(input=[text], model=model).data[0].embedding

embedding_service = EmbeddingService()
