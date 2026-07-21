from dotenv import load_dotenv
import os

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0
)

respuesta = llm.invoke("Di hola")

print(respuesta.content)
