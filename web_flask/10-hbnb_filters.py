#!/usr/bin/python3
"""flask app"""

from flask import Flask
from flask import render_template
from models import storage, State, Amenity


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception=None):
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """return states list"""
    state_list = storage.all(State).values()
    amenity_list = storage.all(Amenity).values()


    return render_template("10-hbnb_filters.html", st_am={'states': state_list, 'amenities': amenity_list})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
