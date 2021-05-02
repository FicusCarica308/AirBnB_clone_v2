#!/usr/bin/python3
"""
Description:
One:
    In this module we start a flask application called flask_app.
within this application we have a single root '/' call. When the user
opens the URL it should return "Hello HBNB!" from def hello_world.

Two:
    The '/hbnb' directory calls function that prints "HBNB".
Does not use strict_slashes=False like Route directory

Application:
    Port = 5000
    Host = 0.0.0.0 (public access)
"""
from flask import Flask
flask_app = Flask(__name__)  # starts flask app


@flask_app.route('/', strict_slashes=False)
def print_greet():
    """ Returns String "Hello HBNB!" when route is landed upon """
    return "Hello HBNB!"


@flask_app.route('/hbnb')
def print_hbnb():
    """ Returns String "HBNB" """
    return "HBNB"


if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=5000)  # sets host and port when main
