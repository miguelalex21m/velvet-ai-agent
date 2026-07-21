import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

data_dir = "data"
persist_dir = "chroma_db"

documents = []

for file in os.listdir(data_dir):
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(data_dir, file))
        documents.extend(loader.load())

if not documents:
    raise RuntimeError("No se encontraron PDFs en la carpeta data.")

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma.from_documents(chunks, embeddings, persist_directory=persist_dir)

print("Base vectorial creada correctamente")
