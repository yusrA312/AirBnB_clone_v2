#!/usr/bin/python3
"""Start web application with two routings
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def HiYsraaa():
    return "Hello HBNB!"


@app.route("/hbnb")
def HB():
    return "HBNB"


@app.route("/c/<text>")
def CCc(text):
    return "C " + text.replace("_", " ")


@app.route("/python/")
@app.route("/python/<text>")
def yOOL(text="is cool"):
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
