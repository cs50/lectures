from flask import Flask, render_template, request

from cs50 import eprint, SQL

app = Flask(__name__)

db = SQL("sqlite:///../lecture.db")

@app.route("/")
def index():
    query = request.args.get("q")
    eprint(query)
    rows = db.execute("SELECT * FROM Album WHERE Title = :q", q=query)
    return render_template("index.html", albums=rows)
