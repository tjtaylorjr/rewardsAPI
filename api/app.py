# This file contains the app function responsible for creating the app object

from flask import Flask
from config import config


def create_app(__name__):
    app = Flask(__name__)
    app.config.update(**config)

    return app
