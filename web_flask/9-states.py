#!/usr/bin/python3
"""flask app"""

from flask import Flask
from flask import render_template
from models import storage, State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception=None):
    storage.close()


@app.route("/states", strict_slashes=False)
def states_list():
    """return states list"""
    state_list = storage.all(State).values()

    return render_template("9-states.html", states=state_list)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """return states with id"""
    state_list = storage.all(State).values()
    states = False
    for x in state_list:
        if x.id == id:
            states = x
            break

    return render_template("9-states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
