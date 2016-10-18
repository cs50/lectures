from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "thisiscs50"

@app.route("/store", methods=["GET", "POST"])
def store():
    if request.method == "POST":
        for pet in ["cat", "hamster", "jellyfish"]:
            if pet not in session:
                session[pet] = int(request.form[pet])
            else:
                session[pet] += int(request.form[pet])
    return render_template("store.html")

@app.route("/cart")
def cart():
    cart = []
    for pet in ["cat", "hamster", "jellyfish"]:
        cart.append({"name":pet.capitalize(), "quantity":session[pet]})
    return render_template("cart.html", cart=cart)
