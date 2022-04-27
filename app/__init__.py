#!/user/bin/env python 3
# -*- codeing utf8 -*-
"""Sample hello world flask app"""

from flask import flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1> Hellow world <h1/>"