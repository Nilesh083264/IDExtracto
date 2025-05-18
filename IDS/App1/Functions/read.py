import os
import fitz  # PyMuPDF
import docx  # python-docx
import pytesseract
from PIL import Image

# Optional: Set path to Tesseract executable if not in PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_image(file_path):
    with Image.open(file_path) as img:
        return pytesseract.image_to_string(img)

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return extract_text_from_pdf(file_path)
    elif ext == '.docx':
        return extract_text_from_docx(file_path)
    elif ext in ['.jpg', '.jpeg', '.png']:
        return extract_text_from_image(file_path)
    else:
        return f"Unsupported file type: {ext}"

def get_texts(path):
    file_path = path
    if os.path.exists(file_path):
        text = extract_text(file_path)
        return text
        # print("\nExtracted Text:\n", text)
    else:
        print("File not found!")
        return "file not found"

