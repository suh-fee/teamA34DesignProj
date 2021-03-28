"""
This file contains all non-auth routes for Flare
"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from __init__ import db, create_app

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


app = create_app()

if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode