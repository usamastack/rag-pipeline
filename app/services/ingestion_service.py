from app.services.extraction_service import extraction_service
from app.services.chunking_service import chunking_service
from app.services.embedding_service import embedding_service
from app.services.vector_store import vector_store
import uuid

class IngestionService:
    @staticmethod
    async def process_file(file_content: bytes, filename: str):
        # 1. Extract Text
        text = await extraction_service.extract_text(file_content, filename)
        if not text:
            raise ValueError("Could not extract text from file")

        # 2. Chunk Text
        chunks = chunking_service.chunk_text(text)

        # 3. Embed and Upsert
        vectors = []
        for i, chunk in enumerate(chunks):
            embedding = embedding_service.get_embedding(chunk)
            
            vector_id = str(uuid.uuid4())
            metadata = {
                "filename": filename,
                "chunk_id": i,
                "text": chunk,
                "source": filename
            }
            
            vectors.append({
                "id": vector_id,
                "values": embedding,
                "metadata": metadata
            })

            # Batch upsert if needed, keeping it simple for now
        
        if vectors:
            vector_store.upsert_vectors(vectors)
        
        return len(vectors)

ingestion_service = IngestionService()
