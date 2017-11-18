from flask import Flask, redirect, render_template, request

# Configure app
app = Flask(__name__)

# Registrants
students = []

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/registrants")
def registrants():
    return render_template("registrants.html", students=students)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    if not name or not dorm:
        return render_template("failure.html")
    students.append(f"{name} from {dorm}")
    return redirect("/registrants")
