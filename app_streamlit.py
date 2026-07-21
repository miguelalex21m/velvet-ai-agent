import streamlit as st
from src.agent import VelvetSpaAgent

st.set_page_config(
    page_title="Velvet Spa AI Agent",
    page_icon="🧴",
    layout="centered"
)

st.title("🧴 Velvet Spa AI Agent")
st.markdown("""
Haz preguntas sobre servicios, políticas o reportes del negocio.
El agente responderá basándose en la información de los documentos corporativos.
""")

@st.cache_resource
def load_agent():
    return VelvetSpaAgent("data/knowledge.csv")

agent = load_agent()

question = st.text_input(
    "Escribe tu pregunta:",
    placeholder="Ejemplo: ¿Qué servicios ofrece Velvet Spa?",
    key="question_input"
)

if st.button("Preguntar", key="ask_button"):
    if question:
        with st.spinner("Procesando tu pregunta..."):
            answer = agent.answer(question)
        st.success("Respuesta:")
        st.write(answer)
    else:
        st.warning("Por favor, escribe una pregunta.")

st.markdown("---")
st.markdown("### Ejemplos de preguntas:")
examples = [
    "¿Qué servicios ofrece Velvet Spa?",
    "¿Cuál es la política de clientes?",
    "¿Cómo están los ingresos financieros?",
    "¿Cuál es el horario de atención?"
]

for example in examples:
    st.markdown(f"- {example}")
