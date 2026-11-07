# Says hello to world by returning a string of HTML

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return '<!DOCTYPE html><html lang="en"><head><title>hello</title></head><body>hello, world</body></html>'
