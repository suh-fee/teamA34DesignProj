"""
This is the file containining the function to create the Blueprints and
initialize the Flare app.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy to manage the Database
db = SQLAlchemy()


def create_app():
    """
    The purpose of this function is to initialize the Flask app and add
    the Blueprints of the main and auth modules.
    """
    app = Flask(__name__)

    # Used by Flask to secure data
    app.config['SECRET_KEY'] = 'super-secret-secure-key'
    # Path to save the Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    # Initialize the Database
    db.init_app(app)

    from source.models import manage_login
    manage_login(app)

    # Blueprint for auth routes
    from source.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Blueprint for non-auth routes
    from source.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
