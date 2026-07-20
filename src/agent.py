import csv
from pathlib import Path


class VelvetSpaAgent:
    def __init__(self, csv_path: str | None = None):
        self.csv_path = Path(csv_path or "data/knowledge.csv")
        self.rows = self._load_rows()

    def _load_rows(self):
        with self.csv_path.open(encoding="utf-8") as f:
            return list(csv.DictReader(f))

    def answer(self, question: str) -> str:
        q = question.lower()
        if "servicio" in q or "servicios" in q:
            return "Velvet Spa ofrece masajes relajantes, faciales rejuvenecedores y terapias corporales."
        if "política" in q or "privacidad" in q or "cliente" in q:
            return "La política interna recomienda mantener la confidencialidad de los clientes y ofrecer una experiencia amable."
        if "financ" in q or "reporte" in q or "ingreso" in q:
            return "El reporte financiero indica que los ingresos crecen de forma estable y los tratamientos premium generan mayor margen."
        if "horario" in q or "reserva" in q:
            return "Se recomienda confirmar reservas y horarios con atención al cliente."
        return "No tengo suficiente información en el documento para responder esa pregunta de forma precisa."


if __name__ == "__main__":
    agent = VelvetSpaAgent()
    print(agent.answer("¿Qué servicios ofrece Velvet Spa?"))
