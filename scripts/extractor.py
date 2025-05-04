import os
from pathlib import Path
from pdfminer.high_level import extract_text


def extract_text_from_pdf(pdf_path):
    """
    Extracts plain text from a PDF file using pdfminer.six.
    Returns the extracted text as a string.
    """
    try:
        text = extract_text(pdf_path)
        return text.strip()
    except Exception as e:
        print(f"[ERROR] Failed to extract text from PDF: {pdf_path}")
        print(f"[EXCEPTION] {e}")
        return ""


def extract_text_from_txt(txt_path):
    """
    Reads plain text directly from a .txt file.
    """
    try:
        with open(txt_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except Exception as e:
        print(f"[ERROR] Failed to read text file: {txt_path}")
        print(f"[EXCEPTION] {e}")
        return ""


def extract_text_generic(file_path):
    """
    Determines file type and extracts text accordingly.
    """
    ext = Path(file_path).suffix.lower()

    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".txt":
        return extract_text_from_txt(file_path)
    else:
        print(f"[WARN] Unsupported file type: {file_path}")
        return ""
