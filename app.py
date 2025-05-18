from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html>
<head>
    <title>Real Estate Search</title>
<style>
    body {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        height: 100vh;
        font-family: Arial, sans-serif;
        background-color: #f9f9f9;
        padding-top: 15vh;
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
        <h2>Введите, что ищете:</h2>
        <form method="post">
            <input type="text" name="query" placeholder="например: 2-комн до 60000 в центре">
            <button type="submit">Найти</button>
        </form>
        {% if result %}
        <h3>Вы ввели:</h3>
        <p>{{ result }}</p>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        result = request.form.get("query")
    return render_template_string(HTML_FORM, result=result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
