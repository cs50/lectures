import csv
import os
import urllib.request

from flask import Flask, jsonify, render_template, request
from flask.exthook import ExtDeprecationWarning
from warnings import simplefilter
simplefilter("ignore", ExtDeprecationWarning)
from flask_autoindex import AutoIndex

app = Flask(__name__)
AutoIndex(app, browse_root=os.path.curdir)

@app.route("/quote")
def quote():
    url = "http://download.finance.yahoo.com/d/quotes.csv?f=snl1&s={}".format(request.args.get("symbol"))
    webpage = urllib.request.urlopen(url)
    datareader = csv.reader(webpage.read().decode("utf-8").splitlines())
    row = next(datareader)
    return jsonify({"name": row[1], "price": float(row[2]), "symbol": row[0].upper()})

@app.route("/register")
def register():
    return render_template("register.html")
