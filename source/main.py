"""
This file contains all non-auth routes for Flare
"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from __init__ import db, create_app
from models import User

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    #TODO: Create SNS Table in DB and template this
    #TODO: Allow users to add their own SNS
    links = [
        {'site': 'Twitter', 'url': 'https://twitter.com/nyuniversity'},
        {'site': 'Instagram', 'url': 'https://twitter.com/nyuniversity'}
    ]
    return render_template('profile.html', user=current_user, links=links)


app = create_app()

if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode