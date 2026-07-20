from flask import Flask, render_template_string, request
from src.agent import VelvetSpaAgent

app = Flask(__name__)
agent = VelvetSpaAgent("data/knowledge.csv")

HTML = """
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Velvet Spa AI Agent</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 40px; background: #fff6f2; color: #4b2e2e; }
      .box { background: white; padding: 20px; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); max-width: 700px; }
      input, button { padding: 10px; margin-top: 10px; width: 100%; }
      button { background: #c97c5d; color: white; border: none; cursor: pointer; }
      .answer { margin-top: 20px; padding: 12px; background: #fcefe8; border-radius: 8px; }
    </style>
  </head>
  <body>
    <div class="box">
      <h1>Velvet Spa AI Agent</h1>
      <p>Haz preguntas sobre servicios, políticas o reportes del negocio.</p>
      <form method="post">
        <input name="question" placeholder="Ejemplo: ¿Qué servicios ofrece Velvet Spa?" required>
        <button type="submit">Preguntar</button>
      </form>
      {% if answer %}
        <div class="answer"><strong>Respuesta:</strong> {{ answer }}</div>
      {% endif %}
    </div>
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form.get("question", "")
        answer = agent.answer(question)
    return render_template_string(HTML, answer=answer)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
