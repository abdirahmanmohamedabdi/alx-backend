#!/usr/bin/env python3
"""
A basic Flask app
"""
from flask import Flask
from flask import request
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# instantiate the Flask app
app = Flask(__name__)
app.config.from_object(Config)

# wrap the application with the Babel
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """
    Renders a basic html template
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)
