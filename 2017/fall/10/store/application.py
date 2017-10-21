from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)

# Configure sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/update", methods=["POST"])
def update():
    for item in ["foo", "bar", "baz"]:
        if item not in session:
            session[item] = int(request.form[item])
        else:
            session[item] += int(request.form[item])
    return redirect("/cart")


@app.route("/cart")
def cart():
    cart = []
    for item in ["foo", "bar", "baz"]:
        cart.append({"name": item, "quantity": session[item]})
    return render_template("cart.html", cart=cart)
