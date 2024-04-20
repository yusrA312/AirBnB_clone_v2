#!/usr/bin/python3
"""This is a script that starts a Flask web application"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hiyusra():
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def yHB():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def CyC(text):
    xt = text.replace('_', ' ')
    return 'C ' + xt


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def YOOL(text='is cool'):
    return 'Python ' + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def NyA(n):
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def ynue(n):
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
