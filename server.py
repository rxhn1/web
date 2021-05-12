from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def home():
  if request.method == "GET":
    return "Hello, World!"

if __name__ == "__main__":
  app.run("0.0.0.0")