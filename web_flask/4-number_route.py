#!/usr/bin/python3
"""This module starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hiyusra():
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def HYB():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def CyC(text):
    t = text.replace('_', ' ')
    return 'C ' + t


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def YOOL(text='is cool'):
    return 'Python ' + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def YNA(n):
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
