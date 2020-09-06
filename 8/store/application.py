from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "shhh"

@app.route("/", methods=["GET", "POST"])
def store():
    if request.method == "POST":
        for item in ["foo", "bar", "baz"]:
            if item not in session:
                session[item] = int(request.form[item])
            else:
                session[item] += int(request.form[item])
        return redirect(url_for("cart"))
    return render_template("store.html")

@app.route("/cart")
def cart():
    cart = []
    for item in ["foo", "bar", "baz"]:
        cart.append({"name": item.capitalize(), "quantity": session[item]})
    return render_template("cart.html", cart=cart)
