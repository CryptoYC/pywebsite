from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# db variable initialization
db = SQLAlchemy()


def create_app():
    """
    Initialize the core app.
    """
    app = Flask(__name__)
    # Initialize Config
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        from . import views
        return app
