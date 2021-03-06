from flask import Flask

from .config import configure
from .models import db


def create_app(config):
    app = Flask(__name__)
    configure(app, config)

    db.init_app(app)

    return app
