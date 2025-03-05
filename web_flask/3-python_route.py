#!/usr/bin/python3
"""Flask app"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """return the home"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """return the home"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """return response"""
    output = ""
    for x in text:
        if x == '_':
            output += ' '
        else:
            output += x
    return "C {}".format(output)


@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    """return response"""
    output = text.replace('_', ' ')
    return "Python {}".format(output)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
