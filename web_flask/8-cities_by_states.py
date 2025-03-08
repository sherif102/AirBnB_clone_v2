#!/usr/bin/python3
"""flask app"""

from flask import Flask
from flask import render_template
from models import storage, State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception=None):
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """return states list"""
    state_list = storage.all(State).values()

    return render_template("8-cities_by_states.html", states=state_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
