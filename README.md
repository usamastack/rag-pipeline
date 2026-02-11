# RAG Backend with FastAPI & Pinecone

A high-performance, modular backend for Building RAG (Retrieval-Augmented Generation) applications. Built with **FastAPI**, **Pinecone**, and **OpenAI**.

## 🚀 Features

### 📄 Document Processing Pipeline
- **Multi-Format Support**: 
  - `PDF` (via `pypdf`)
  - `DOCX` (via `python-docx`)
  - `TXT`, `MD`
  - `Images` (PNG, JPG via `pytesseract` OCR)
- **Intelligent Chunking**: Recursive character splitting to maintain context.
- **Vector Ingestion**: Automatic embedding generation and upsert to Pinecone.

### 🧠 Intelligent Q&A
- **Context-Aware Chat**: Remembers conversation history (session-based).
- **Hybrid Retrieval**: Semantic search using OpenAI embeddings.
- **Source Attribution**: Returns exact text snippets and file references for every answer.
- **Citation Support**: Answers are grounded in your data.

### ⚡ Advanced Capabilities
- **Multi-LLM Comparison**: Run the same query against multiple models (GPT-4, GPT-3.5, etc.) in parallel.
- **Analytics**: Track usage and most queried topics.
- **Modular Architecture**: Clean separation of concerns (Services, API, Models, Core).

---

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Vector Database**: Pinecone
- **LLM**: OpenAI (GPT-4 / GPT-3.5)
- **Embedding**: OpenAI `text-embedding-ada-002`
- **OCR**: Tesseract & Pytesseract
- **Language**: Python 3.10+

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/rag-backend-fastapi.git
cd rag-backend-fastapi
```

### 2. Set Up Environment
Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Copy the example environment file:
```bash
cp .env.example .env
```
Edit `.env` with your API keys:
```env
OPENAI_API_KEY=sk-...
PINECONE_API_KEY=...
PINECONE_ENV=gcp-starter
PINECONE_INDEX_NAME=rag-documents
```

> **Note**: For OCR, ensure Tesseract is installed on your system.
> - **macOS**: `brew install tesseract`
> - **Ubuntu**: `sudo apt-get install tesseract-ocr`
> - **Windows**: Download installer from UB-Mannheim

---

## 🐳 Docker Support

Run the application with a single command:

```bash
# Build and start
make up

# View logs
make logs

# Stop
make down
```

Or using standard Docker Compose:
```bash
docker-compose up --build -d
```

---

## 🏃‍♂️ Usage

Start the development server:
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000`.

### 📚 API Documentation
Interactive docs are available at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

---

## 🔌 Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `POST` | `/api/v1/upload` | Upload PDF/DOCX/Images for ingestion |
| `POST` | `/api/v1/chat` | Chat with your documents (RAG) |
| `POST` | `/api/v1/compare` | Compare answers across multiple LLMs |
| `GET` | `/api/v1/analytics` | Get usage statistics |

---

## 📂 Project Structure

```
rag-backend-fastapi/
├── app/
│   ├── api/            # API Endpoints
│   ├── core/           # Config & Settings
│   ├── models/         # Pydantic Schemas
│   ├── services/       # Business Logic (OCR, RAG, LLM)
│   └── utils/          # Helper functions
├── data/               # Local data storage
├── requirements.txt    # Dependencies
└── .env                # Secrets
```

---

## 🤝 Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
