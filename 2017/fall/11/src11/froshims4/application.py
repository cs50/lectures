from cs50 import SQL
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

db = SQL("sqlite:///froshims4.db")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        if not request.form.get("name") or not request.form.get("dorm"):
            return render_template("failure.html")
        db.execute("INSERT INTO registrants (name, dorm) VALUES(:name, :dorm)",
                   name=request.form.get("name"), dorm=request.form.get("dorm"))
        return render_template("success.html")


@app.route("/registrants")
def registrants():
    rows = db.execute("SELECT * FROM registrants")
    return render_template("registrants.html", registrants=rows)


@app.route("/unregister", methods=["GET", "POST"])
def unregister():
    if request.method == "GET":
        rows = db.execute("SELECT * FROM registrants")
        return render_template("unregister.html", registrants=rows)
    elif request.method == "POST":
        if request.form["id"]:
            db.execute("DELETE FROM registrants WHERE id = :id", id=request.form.get("id"))
        return redirect("/")
