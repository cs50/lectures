from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///store.db")

# Configure sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/books")
def books():
    session["cart"] = []
    books = db.execute("SELECT * FROM books");
    return render_template("books.html", books=books)


@app.route("/books/<id>")
def book(id):
    books = db.execute("SELECT * FROM books WHERE id = ?", id)
    return render_template("book.html", book=books[0])


@app.route("/cart", methods=["GET", "POST"])
def cart():

    # POST
    if request.method == "POST":
        id = request.form.get("id")
        if id:
            session["cart"].append(id)
        return redirect("/cart")

    # GET
    books = db.execute("SELECT * FROM books")
    return render_template("cart.html", books=books, cart=session["cart"])
