# This file contains the app function responsible for creating the app object

from flask import Flask


def create_app(__name__):
    app = Flask(__name__)

    return app
