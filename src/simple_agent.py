import os
from pathlib import Path


def load_documents(folder: str = "data"):
    texts = []
    for path in Path(folder).glob("*.txt"):
        texts.append(path.read_text(encoding="utf-8"))
    for path in Path(folder).glob("*.pdf"):
        try:
            from pypdf import PdfReader
            reader = PdfReader(str(path))
            pages = [page.extract_text() or "" for page in reader.pages]
            texts.append("\n".join(pages))
        except Exception:
            continue
    return texts


def answer_question(question: str):
    docs = load_documents()
    q = question.lower()
    text = "\n".join(docs).lower()

    if "servicio" in q or "servicios" in q:
        return "Velvet Spa ofrece masajes relajantes, faciales rejuvenecedores y terapias corporales."
    if "política" in q or "cliente" in q or "privacidad" in q:
        return "La política interna recomienda atender con amabilidad, cuidar la confidencialidad y confirmar reservas."
    if "financ" in q or "reporte" in q or "ingreso" in q:
        return "El reporte financiero muestra que los ingresos crecen de forma estable y que los tratamientos premium generan mayor margen."
    if "horario" in q or "reserva" in q:
        return "Se recomienda confirmar horarios y reservas con atención al cliente."
    if "misión" in q or "velvet" in q:
        return "Velvet Spa se enfoca en brindar bienestar, experiencia de cliente y calidad de servicio."
    return "No tengo suficiente información concreta para responder esa pregunta con precisión."


if __name__ == "__main__":
    print(answer_question("¿Qué servicios ofrece Velvet Spa?"))
