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


@flask_app.route('/states', strict_slashes=False)
def display_states():
    """ displays all states in db_storage """
    states = storage.all(State)
    return render_template('9-states.html', states=states, check=0)


@flask_app.route('/states/<id>', strict_slashes=False)
def display_state(id):
    """ displays all states in db_storage """
    states = storage.all(State)
    exist = 0  # Not found by default
    state_hold = None
    change_cities = None

    for state in states.values():
        if state.id == id:
            exist = 1  # 1 for found
            state_hold = state

    if exist == 1:
        cities = storage.all(City)
        change_cities = dict(cities)
        for key, city in cities.items():
            if city.state_id != id:
                change_cities.pop(key)

    return render_template('9-states.html', state_hold=state_hold, check=1,
                           exist=exist, cities=change_cities)


@flask_app.teardown_appcontext
def sessions_close(self):
    """ closes the current open storage sessions """
    storage.close()

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=5000)  # sets host and port when main
