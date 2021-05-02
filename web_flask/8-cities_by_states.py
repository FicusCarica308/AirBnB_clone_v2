#!/usr/bin/python3
"""
Description:

Application:
    Port = 5000
    Host = 0.0.0.0 (public access)
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
flask_app = Flask(__name__)  # starts flask app


@flask_app.route('/states_list', strict_slashes=False)
def render_html():
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@flask_app.route('/cities_by_states', strict_slashes=False)
def render_by_states():
    """ Temp description """
    states = storage.all(State)
    cities = storage.all(City)
    return render_template("8-cities_by_states.html", states=states,
                           cities=cities)


@flask_app.teardown_appcontext
def sessions_close(self):
    """ closes the current open storage sessions """
    storage.close()

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=5000)  # sets host and port when main
