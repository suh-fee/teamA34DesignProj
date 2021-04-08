"""
This is the file containining all of the non-auth routes for Flare app.
"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from __init__ import db, create_app
from models import User

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """
    The purpose of this function is to render the main page of the site.
    """
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    """
    The purpose of this function is to render the profile page for each user.
    It requires the user to be logged into their account before they can view
    their own profile.
    """
    #TODO: Create SNS Table in DB and template this
    #TODO: Allow users to add their own SNS
    #TODO: Allow users that are not logged in to view certain parts of another
    # user's profile
    links = [
        {'site': 'Twitter', 'url': 'https://twitter.com/nyuniversity'},
        {'site': 'Instagram', 'url': 'https://www.instagram.com/nyuniversity'}
    ]
    return render_template('profile.html', user=current_user, links=links)


app = create_app()

if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode