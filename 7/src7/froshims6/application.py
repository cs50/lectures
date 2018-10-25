from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("dorm"):
        return render_template("failure.html")
    with open("registered.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "dorm"])
        writer.writerow({"name": request.form.get("name"), "dorm": request.form.get("dorm")})
    return render_template("success.html")


@app.route("/registered")
def registered():
    with open("registered.csv", "r") as file:
        reader = csv.DictReader(file)
        students = list(reader)
    return render_template("registered.html", students=students)
