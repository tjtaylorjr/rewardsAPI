import flask
from api import app

app = app.create_app(__name__)


if __name__ == '__main__':
    app.run(port=app.config['PORT'])
