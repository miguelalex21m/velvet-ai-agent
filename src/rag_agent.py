from pathlib import Path
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_google_genai.embeddings import GoogleGenerativeAIEmbeddings

load_dotenv()


def build_agent(data_dir: str = "data"):
    docs = []
    for path in Path(data_dir).glob("*.txt"):
        loader = TextLoader(str(path), encoding="utf-8")
        docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=120)
    chunks = splitter.split_documents(docs)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    vector_store = Chroma.from_documents(chunks, embeddings, persist_directory="chroma_db")

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    return vector_store, llm


def ask(question: str, data_dir: str = "data"):
    vector_store, llm = build_agent(data_dir)
    docs = vector_store.similarity_search(question, k=3)
    context = "\n\n".join(doc.page_content for doc in docs)
    prompt = f"Responde la pregunta usando solo la información del contexto.\n\nPregunta: {question}\n\nContexto: {context}"
    return llm.invoke(prompt).content
