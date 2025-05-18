from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_FORM = """
<!DOCTYPE html>
<html>
<head><title>Real Estate Search</title></head>
<body>
    <h2>Введите, что ищете:</h2>
    <form method="post">
        <input type="text" name="query" placeholder="например: 2-комн до 60000 в центре" size="50">
        <button type="submit">Найти</button>
    </form>
    {% if result %}
    <h3>Вы ввели:</h3>
    <p>{{ result }}</p>
    {% endif %}
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
    app.run(host="0.0.0.0", port=10000)
