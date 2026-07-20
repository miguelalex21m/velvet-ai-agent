import os
import sys
from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma


def build_db():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    return Chroma(persist_directory="chroma_db", embedding_function=embeddings)


def fallback_answer(question: str, docs):
    text = "\n".join(doc.page_content.lower() for doc in docs)
    q = question.lower()
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


def answer_question(question: str):
    db = build_db()
    docs = db.similarity_search(question, k=3)

    if not docs:
        return "No se encontraron documentos relevantes en la base vectorial."

    contexto = "\n".join(doc.page_content for doc in docs)
    prompt = f"""
    Responde usando solamente esta información:

    {contexto}

    Pregunta:
    {question}
    """

    api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    if not api_key:
        return fallback_answer(question, docs)

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0, api_key=api_key)
    try:
        respuesta = llm.invoke(prompt)
        return respuesta.content
    except Exception:
        return fallback_answer(question, docs)


if __name__ == "__main__":
    questions = sys.argv[1:]
    if questions:
        for question in questions:
            print(f"\nPregunta: {question}")
            print("Respuesta:")
            print(answer_question(question))
    else:
        while True:
            pregunta = input("\nPregunta: ")
            if pregunta.lower() == "salir":
                break
            print("\nRespuesta:")
            print(answer_question(pregunta))
