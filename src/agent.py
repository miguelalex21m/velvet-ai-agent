import os
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_community.document_loaders import PyPDFLoader, CSVLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()


class VelvetSpaAgent:
    def __init__(self, csv_path: str | None = None):
        # Obtener API key
        api_key = os.getenv("GOOGLE_API_KEY")
        
        # Configurar API key de Google
        genai.configure(api_key=api_key)
        
        # Cargar documentos
        documents = []
        
        # Cargar PDFs del directorio data/
        data_dir = "data"
        if os.path.exists(data_dir):
            for file in os.listdir(data_dir):
                file_path = os.path.join(data_dir, file)
                if file.endswith('.pdf'):
                    loader = PyPDFLoader(file_path)
                    documents.extend(loader.load())
                elif file.endswith('.csv'):
                    loader = CSVLoader(file_path)
                    documents.extend(loader.load())
        
        # Si no hay documentos, crear uno de ejemplo
        if not documents:
            from langchain.schema import Document
            documents = [
                Document(page_content="Velvet Spa ofrece servicios de masajes, faciales y tratamientos de bienestar. Horario: 9am-6pm de lunes a sábado.", metadata={"source": "ejemplo"})
            ]
        
        # Dividir documentos en chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.texts = text_splitter.split_documents(documents)
        
        # Inicializar LLM
        self.model = genai.GenerativeModel('gemini-flash-latest')

    def answer(self, question: str) -> str:
        try:
            # Búsqueda simple por palabras clave en los documentos
            question_lower = question.lower()
            relevant_docs = []
            
            for doc in self.texts:
                content_lower = doc.page_content.lower()
                # Buscar coincidencias de palabras clave
                words = question_lower.split()
                matches = sum(1 for word in words if word in content_lower)
                if matches > 0:
                    relevant_docs.append((doc, matches))
            
            # Ordenar por número de coincidencias
            relevant_docs.sort(key=lambda x: x[1], reverse=True)
            
            if not relevant_docs:
                return "No encontré información relevante en los documentos para responder esa pregunta."
            
            # Tomar los 3 documentos más relevantes
            top_docs = [doc for doc, _ in relevant_docs[:3]]
            
            # Crear contexto con los documentos encontrados
            context = "\n\n".join(doc.page_content for doc in top_docs)
            
            # Crear prompt para el LLM
            prompt = f"""Eres un asistente útil de Velvet Spa. Responde la pregunta usando SOLO la información del contexto proporcionado.
            
Pregunta: {question}

Contexto:
{context}

Respuesta:"""
            
            # Invocar al LLM
            response = self.model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            return f"Error al procesar la pregunta: {str(e)}"


if __name__ == "__main__":
    agent = VelvetSpaAgent()
    print(agent.answer("¿Qué servicios ofrece Velvet Spa?"))
