from cs50 import SQL
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

db = SQL("sqlite:///froshims2.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    if request.form["name"] == "" or request.form["dorm"] == "":
        return render_template("failure.html")
    db.execute("INSERT INTO registrants (name, dorm) VALUES(:name, :dorm)", name=request.form["name"], dorm=request.form["dorm"])
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
            db.execute("DELETE FROM registrants WHERE id = :id", id=request.form["id"])
        return redirect(url_for("registrants"))