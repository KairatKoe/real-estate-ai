from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Kairat! Your service is live."

if __name__ == "__main__":
    app.run()
