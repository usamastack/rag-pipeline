from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.ingestion_service import ingestion_service

router = APIRouter()

@router.post("/upload", tags=["Ingestion"])
async def upload_file(file: UploadFile = File(...)):
    try:
        content = await file.read()
        num_chunks = await ingestion_service.process_file(content, file.filename)
        return {
            "filename": file.filename, 
            "status": "success", 
            "chunks_processed": num_chunks
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
