# This file contains the app function responsible for creating the app object

from flask import Flask
from config import config
from controllers import errors, ledger, root


def create_app(__name__):
    app = Flask(__name__)
    app.config.update(**config)
    app.register_blueprint(errors)
    app.register_blueprint(ledger)
    app.register_blueprint(root)

    return app
