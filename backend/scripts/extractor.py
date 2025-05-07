from pathlib import Path
from pdfminer.high_level import extract_text
from docx import Document


def extract_text_from_pdf(pdf_path):
    try:
        text = extract_text(pdf_path)
        print(f"[INFO] Extracted PDF: {pdf_path} ({len(text)} chars)")
        return text.strip()
    except Exception as e:
        print(f"[ERROR] Failed to extract text from PDF: {pdf_path}")
        print(f"[EXCEPTION] {e}")
        return ""


def extract_text_from_txt(txt_path):
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            text = file.read()
            print(f"[INFO] Extracted TXT: {txt_path} ({len(text)} chars)")
            return text.strip()
    except Exception as e:
        print(f"[ERROR] Failed to read text file: {txt_path}")
        print(f"[EXCEPTION] {e}")
        return ""


def extract_text_from_docx(docx_path):
    try:
        doc = Document(docx_path)
        full_text = [para.text for para in doc.paragraphs]
        result = '\n'.join(full_text).strip()
        print(f"[INFO] Extracted DOCX: {docx_path} ({len(result)} chars)")
        return result
    except Exception as e:
        print(f"[ERROR] Failed to read DOCX file: {docx_path}")
        print(f"[EXCEPTION] {e}")
        return ""


def extract_text_generic(file_path):
    ext = Path(file_path).suffix.lower()

    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".txt":
        return extract_text_from_txt(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    else:
        print(f"[WARN] Unsupported file type: {file_path}")
        return ""
