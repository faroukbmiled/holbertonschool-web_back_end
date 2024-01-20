#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup, Get locale from request """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
"""Babel object"""


class Config(object):
    """class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
"""class config"""


@app.route('/')
def root():
    """app.py"""
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """ to determine the best match with our supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
