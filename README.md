# Velvet Spa AI Agent

Este proyecto desarrolla un agente de inteligencia artificial capaz de responder preguntas sobre documentos internos del negocio Velvet Spa utilizando IA y procesamiento de documentos.

## Objetivo

Permitir que colaboradores consulten información de manera natural, sin abrir manuales ni reportes, mediante preguntas como:

- ¿Qué servicios ofrece Velvet Spa?
- ¿Cuál es la política de atención al cliente?
- ¿Qué información aparece en el reporte financiero?

## Estructura del proyecto

```text
velvet-ai-agent/
├── data/
├── src/
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Tecnologías utilizadas

- Python
- LangChain
- OpenAI / modelos LLM
- PyPDF
- FAISS
- dotenv

## Cómo ejecutar

1. Crear y activar el entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Agregar tu API key en el archivo `.env`.
4. Ejecutar el agente desde la carpeta `src`.

## Ejemplos de preguntas

- ¿Qué servicios ofrece Velvet Spa?
- ¿Cuál es la política de atención al cliente?
- ¿Qué información contiene el reporte financiero?

## Ejemplos de respuestas esperadas

El agente responderá con información extraída del contenido de los documentos cargados.
