from pathlib import Path
from load_documents import load_pdf_text

if __name__ == "__main__":
    data_path = Path(__file__).resolve().parent.parent / "data" / "sample_knowledge.txt"
    print("Archivo cargado:", data_path)
    text = load_pdf_text(str(data_path)) if data_path.suffix.lower() == ".pdf" else data_path.read_text(encoding="utf-8")
    print(text[:1000])
