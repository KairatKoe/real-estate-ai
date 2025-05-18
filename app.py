from flask import Flask, request, render_template_string
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")


HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Real Estate AI Search</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: flex-start;
            height: 100vh;
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            padding-top: 22vh;
        }
        .form-box {
            text-align: center;
        }
        input[type="text"] {
            width: 400px;
            padding: 10px;
            font-size: 16px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
        }
        h2, h3 {
            color: #333;
        }
    </style>
</head>
<body>
    <div class="form-box">
        <h2>Что вы ищете?</h2>
        <form method="post">
            <input type="text" name="query" placeholder="например: 2-комн юг до 50000">
            <button type="submit">Найти</button>
        </form>
        {% if result %}
        <h3>GPT-понимание:</h3>
        <p>{{ result }}</p>
        {% endif %}
    </div>
</body>
</html>
"""

def gpt_interpret(user_input):
    prompt = f"""Пользователь написал запрос о недвижимости: "{user_input}". 
Преобразуй его в полный, понятный, вежливый текст как для агента по недвижимости. 
Пиши по-русски. Не добавляй лишнего. Просто уточни смысл в полной форме."""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты помощник по поиску недвижимости. Отвечай по-русски, в корректной, полной форме."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
            max_tokens=100
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Ошибка: {str(e)}"


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        query = request.form.get("query")
        if query:
            result = gpt_interpret(query)
    return render_template_string(HTML_FORM, result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
