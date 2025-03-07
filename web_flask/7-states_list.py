#!/usr/bin/python3
"""flask app"""

from flask import Flask
from flask import render_template
from models import storage, State


app = Flask(__name__)

@app.teardown_appcontext
def close_connection(self):
    """close connection"""
    storage.close()

@app.route("/states_list", strict_slashes=False)
def states_list():
    """return states list"""
    state_list = storage.all()
    names = [{'id':'3', 'name':'taye'}, {'id':'2', 'name':'idowu'}, {'id':'1', 'name':'alaba'}, {'id':'4', 'name':'kehinde'}]

    return render_template("7-states_list.html", context=state_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
