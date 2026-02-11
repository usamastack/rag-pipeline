import re

class ChunkingService:
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_text(self, text: str) -> list[str]:
        # Simple recursive character splitter logic
        separators = ["\n\n", "\n", " ", ""]
        final_chunks = []
        
        # Initial split
        if not text:
            return []

        # This is a simplified version of RecursiveCharacterTextSplitter
        # for maximum code cleanliness and minimum dependencies
        
        # 1. Split by paragraphs
        paragraphs = text.split("\n\n")
        current_chunk = ""
        
        for para in paragraphs:
            if len(current_chunk) + len(para) + 2 <= self.chunk_size:
                current_chunk += para + "\n\n"
            else:
                if current_chunk:
                    final_chunks.append(current_chunk.strip())
                current_chunk = para + "\n\n"
                
                # If paragraph itself is too big, split by lines
                if len(para) > self.chunk_size:
                    # Recursive logic could be here, but keeping it simple for now
                    # Just split the big paragraph into chunks
                    # TODO: enhance with actual recursive logic if needed
                    pass 

        if current_chunk:
            final_chunks.append(current_chunk.strip())

        return final_chunks

chunking_service = ChunkingService()
