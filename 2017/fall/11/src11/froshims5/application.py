from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Flask-SQLAlchemy
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///froshims5.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

class Registrant(db.Model):

    __tablename__ = "registrants"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    dorm = db.Column(db.Text)

    def __init__(self, name, dorm):
        self.name = name
        self.dorm = dorm


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
        registrant = Registrant(request.form.get("name"), request.form.get("dorm"))
        db.session.add(registrant)
        db.session.commit()
        return render_template("success.html")


@app.route("/registrants")
def registrants():
    rows = Registrant.query.all()
    return render_template("registrants.html", registrants=rows)


@app.route("/unregister", methods=["GET", "POST"])
def unregister():
    if request.method == "GET":
        rows = Registrant.query.all()
        return render_template("unregister.html", registrants=rows)
    elif request.method == "POST":
        if request.form.get("id"):
            Registrant.query.filter(Registrant.id == request.form.get("id")).delete()
            db.session.commit()
        return redirect("/")
