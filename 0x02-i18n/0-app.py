#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Renders a basic html template
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
