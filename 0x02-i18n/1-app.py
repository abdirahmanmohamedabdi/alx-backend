#!/usr/bin/env python3
"""
A basic Flask app
"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


class config(object):
    """
    Application configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# instantiate the Flask app
app = Flask(__name__)
app.config.from_object(config)

# wrap the application with the Babel
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """
    Renders a basic html template
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
