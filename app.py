from flask import Flask, request, render_template_string
from dotenv import load_dotenv
import os
import openai

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        user_input = request.form["query"]
        prompt = f"Пользователь написал запрос о недвижимости: \"{user_input}\".\nПреобразуй его в полный, точный, удобный для ИИ текст на русском языке."

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100
            )
            result = response.choices[0].message["content"].strip()
        except Exception as e:
            result = f"Ошибка: {e}"

    return render_template_string("""
    <form method="post">
        <p><b>Введите, что ищете:</b></p>
        <input name="query" style="width:400px;" placeholder="например: 2-комн до 60000 в центре">
        <input type="submit" value="Найти">
    </form>
    {% if result %}
    <p><b>Результат:</b> {{ result }}</p>
    {% endif %}
    """, result=result)

if __name__ == "__main__":
    app.run()
