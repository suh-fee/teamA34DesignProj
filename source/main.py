"""
This is the file containining all of the non-auth routes for Flare app.
"""

from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from source.__init__ import db, create_app
from source.models import User, Site

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
    # TODO: Create SNS Table in DB and template this
    # TODO: Allow users to add their own SNS
    # TODO: Allow users that are not logged in to view certain parts of another
    # user's profile

    return render_template('profile.html', user=current_user,
                           sns=current_user.sns)


@main.route('/add_site')
@login_required
def add_site():
    """
    The purpose of this function is to render the site that allows users to add
    a social networking site associated with their account.
    """
    return render_template('add_site.html')


@main.route('/add_site', methods=['POST'])
@login_required
def add_site_post():
    """
    The purpose of this function is to obtain the information the user submits
    when linking a new social networking site to their profile. This
    information is sent through an HTML POST request and is captured and
    added using the Site model.
    """
    site = request.form.get('sns')
    handle = request.form.get('snsuser')
    link = request.form.get('link')

    new_site = Site(site=site, handle=handle, link=link)
    current_user.sns.append(new_site)

    db.session.add(new_site)
    db.session.commit()

    return redirect(url_for('main.profile'))


app = create_app()

if __name__ == '__main__':
    db.create_all(app=create_app())  # create the SQLite database
    app.run(debug=True)  # run the flask app on debug mode
