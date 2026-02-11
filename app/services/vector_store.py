import os
from pinecone import Pinecone, ServerlessSpec
from app.core.config import get_settings

settings = get_settings()

class VectorStore:
    def __init__(self):
        self.pc = Pinecone(api_key=settings.PINECONE_API_KEY)
        self.index_name = settings.PINECONE_INDEX_NAME
        self._ensure_index_exists()
        self.index = self.pc.Index(self.index_name)

    def _ensure_index_exists(self):
        existing_indexes = [index.name for index in self.pc.list_indexes()]
        if self.index_name not in existing_indexes:
            self.pc.create_index(
                name=self.index_name,
                dimension=1536, # Default for OpenAI text-embedding-ada-002
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region=settings.PINECONE_ENV
                )
            )

    def upsert_vectors(self, vectors, namespace="default"):
        self.index.upsert(vectors=vectors, namespace=namespace)

    def query_vectors(self, vector, top_k=5, namespace="default", filter=None):
        return self.index.query(
            vector=vector,
            top_k=top_k,
            include_metadata=True,
            namespace=namespace,
            filter=filter
        )

# Singleton instance
vector_store = VectorStore()
