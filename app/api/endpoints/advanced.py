from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from app.services.retrieval_service import retrieval_service
from app.services.llm_service import llm_service
import asyncio

router = APIRouter()

class CompareRequest(BaseModel):
    query: str
    models: List[str] = ["gpt-4", "gpt-3.5", "claude-3-opus", "gemini-pro"]

class CompareResponse(BaseModel):
    query: str
    results: List[Dict[str, Any]]

@router.post("/compare", response_model=CompareResponse, tags=["Advanced"])
async def compare_models(request: CompareRequest):
    try:
        # 1. Retrieve Context once
        context_metadatas = retrieval_service.retrieve_context(request.query)
        context_texts = [m.get('text', '') for m in context_metadatas]
        
        # 2. Run in parallel
        tasks = [
            llm_service.generate_answer_with_provider(model, request.query, context_texts)
            for model in request.models
        ]
        
        results = await asyncio.gather(*tasks)
        
        return CompareResponse(
            query=request.query,
            results=results
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/analytics", tags=["Advanced"])
async def get_analytics():
    # Placeholder for analytics
    return {
        "most_queried_topics": ["RAG", "FastAPI", "Python"],
        "total_documents": 5, # Mock
        "average_latency": 1.2
    }
