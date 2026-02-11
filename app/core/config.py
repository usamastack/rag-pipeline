from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "RAG Backend API"
    OPENAI_API_KEY: str
    PINECONE_API_KEY: str
    PINECONE_ENV: str
    PINECONE_INDEX_NAME: str = "rag-documents"

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()
