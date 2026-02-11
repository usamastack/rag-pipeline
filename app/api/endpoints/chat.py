from fastapi import APIRouter, HTTPException
from app.models.chat import ChatRequest, ChatResponse, Source
from app.services.retrieval_service import retrieval_service
from app.services.llm_service import llm_service

router = APIRouter()

# In-memory session storage for portfolio demo
# In production, use Redis or a proper DB
chat_sessions = {}

@router.post("/chat", response_model=ChatResponse, tags=["Chat"])
async def chat_endpoint(request: ChatRequest):
    try:
        # 1. Retrieve Context
        # Returns list of dicts: {'text': ..., 'filename': ..., 'chunk_id': ...}
        context_metadatas = retrieval_service.retrieve_context(request.query)
        
        # Extract just text for LLM
        context_texts = [m.get('text', '') for m in context_metadatas]
        
        # 2. Append to History (Simple)
        history = chat_sessions.get(request.session_id, [])
        history.append({"role": "user", "content": request.query})
        
        # 3. Generate Answer
        # TODO: Integrate history into prompt
        answer = llm_service.generate_answer(request.query, context_texts, model=request.model)
        
        # 4. Update History
        history.append({"role": "assistant", "content": answer})
        chat_sessions[request.session_id] = history
        
        # 5. Format Sources
        sources = [
            Source(
                text=m.get('text', ''), 
                filename=m.get('filename', 'unknown'), 
                chunk_id=int(m.get('chunk_id', 0))
            ) 
            for m in context_metadatas
        ] 
        
        return ChatResponse(
            answer=answer,
            sources=sources,
            session_id=request.session_id
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
