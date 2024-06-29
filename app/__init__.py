from flask import Flask


from .configs import Config
from .extensions import db, migrate

def create_app():
    app = Flask(__name__)
    # set configs
    app.config.from_object(Config)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)