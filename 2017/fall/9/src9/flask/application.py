from flask import Flask, redirect, render_template, session, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
