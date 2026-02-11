from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.api.endpoints import upload, chat, advanced

# Load environment variables
load_dotenv()

app = FastAPI(
    title="RAG Backend API",
    description="Backend for Document Processing and RAG Pipeline",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(upload.router, prefix="/api/v1")
app.include_router(chat.router, prefix="/api/v1")
app.include_router(advanced.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to the RAG Backend API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
