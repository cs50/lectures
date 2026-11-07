# Says hello to world by returning a string of text

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hello, world"
