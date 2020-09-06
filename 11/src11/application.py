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
    symbol = request.args.get("symbol")
    url = f"https://www.alphavantage.co/query?apikey=NAJXWIA8D6VN6A3K&datatype=csv&function=TIME_SERIES_INTRADAY&interval=1min&symbol={symbol}"
    webpage = urllib.request.urlopen(url)
    datareader = csv.reader(webpage.read().decode("utf-8").splitlines())
    next(datareader)
    row = next(datareader)
    return jsonify({
    	"name": symbol.upper(),
        "price": float(row[4]),
        "symbol": symbol.upper()
    })


@app.route("/register")
def register():
    return "You're registered! (Well, not really.)"
