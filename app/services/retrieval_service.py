from app.services.vector_store import vector_store
from app.services.embedding_service import embedding_service

class RetrievalService:
    @staticmethod
    def retrieve_context(self, query: str, top_k: int = 5) -> list[dict]:
        # 1. Generate embedding for query
        query_embedding = embedding_service.get_embedding(query)

        # 2. Query Pinecone
        results = vector_store.query_vectors(
            vector=query_embedding,
            top_k=top_k
        )

        # 3. Extract text and metadata
        contexts = []
        for match in results.matches:
            if match.metadata:
                contexts.append(match.metadata)
        
        return contexts

retrieval_service = RetrievalService()
