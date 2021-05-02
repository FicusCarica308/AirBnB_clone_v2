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

Three:
    The '/c/<text>' will display “C ” followed by the value of the text
variable (replace underscore _ symbols with a space )...
Does not use strict_slashes=False like Route directory

Four:
    The '/python/(<text>)' will display “Python”, followed by the value of
the text variable (replace underscore _ symbols with a space )...
The default value of text is “is cool”

Five:
    The '/number/<n>' will display “n is a number” only if n is an integer

Six:
    The '/number_template/<n>' display a HTML page only if n is an integer

Application:
    Port = 5000
    Host = 0.0.0.0 (public access)
"""
from flask import Flask, render_template
flask_app = Flask(__name__)  # starts flask app


@flask_app.route('/', strict_slashes=False)
def print_greet():
    """ Returns String "Hello HBNB!" when route is landed upon """
    return "Hello HBNB!"


@flask_app.route('/hbnb')
def print_hbnb():
    """ Returns String "HBNB" """
    return "HBNB"


@flask_app.route('/c/<text>')
def print_text(text):
    """ prints out given text using flask variable rules """
    return 'C %s' % text.replace("_", " ")


@flask_app.route('/python', strict_slashes=False)  # so dir doesnt throw 404
@flask_app.route('/python/<text>')
def print_text_default(text='is cool'):
    """ prints out given text using flask variable rules """
    return 'Python %s' % text.replace("_", " ")


@flask_app.route('/number/<int:n>')
def print_if_num(n):
    """ prints out num if it is a number """
    return '%i is a number' % n


@flask_app.route('/number_template/<n>')
def render_html_int(n):
    """ renders html template only if n is a number """
    return render_template('5-number.html', num=n)

if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=5000)  # sets host and port when main
