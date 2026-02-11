import io
from pypdf import PdfReader
from docx import Document
from app.services.ocr_service import ocr_service

class ExtractionService:
    @staticmethod
    async def extract_text(file_bytes: bytes, filename: str) -> str:
        ext = filename.split('.')[-1].lower()
        
        if ext == 'pdf':
            return ExtractionService._extract_from_pdf(file_bytes)
        elif ext in ['docx', 'doc']:
            return ExtractionService._extract_from_docx(file_bytes)
        elif ext in ['txt', 'md']:
            return file_bytes.decode('utf-8')
        elif ext in ['jpg', 'jpeg', 'png']:
            return ocr_service.extract_text_from_image(file_bytes)
        else:
            return ""

    @staticmethod
    def _extract_from_pdf(file_bytes: bytes) -> str:
        text = ""
        try:
            reader = PdfReader(io.BytesIO(file_bytes))
            for page in reader.pages:
                text += page.extract_text() + "\n"
        except Exception as e:
            print(f"Error extracting PDF: {e}")
        return text

    @staticmethod
    def _extract_from_docx(file_bytes: bytes) -> str:
        text = ""
        try:
            doc = Document(io.BytesIO(file_bytes))
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
        except Exception as e:
            print(f"Error extracting DOCX: {e}")
        return text

extraction_service = ExtractionService()
