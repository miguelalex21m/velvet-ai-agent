from langchain_community.document_loaders import PyPDFLoader
import os
from pathlib import Path
from pypdf import PdfReader


def load_pdf_text(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {path}")

    reader = PdfReader(str(path))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    return text


pdf_folder = "data"
documents = []

for file in os.listdir(pdf_folder):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(pdf_folder, file))
        documents.extend(loader.load())

print(f"Documentos cargados: {len(documents)}")
