"""
This is the file containining all of the non-auth routes for Flare app.
"""

from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from source.__init__ import db, create_app
from source.models import User, Site

import tweepy

main = Blueprint('main', __name__)

testaccounts = ["@nimcanttweet", "@twitter"]


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


@main.route('/remove_site')
@login_required
def remove_site():
    """
    The purpose of this function is to render the site that allows users to
    remove social networking site associated with their account.
    """
    return render_template('remove_site.html', sns=current_user.sns)


@main.route('/remove_site', methods=['POST'])
@login_required
def remove_site_post():
    """
    The purpose of this function is to obtain the information the user submits
    when removing new social networking site to their profile. This
    information is sent through an HTML POST request and is captured and
    removed from the database.
    """
    handle = request.form.get('snsuser')

    for i, s in enumerate(current_user.sns):
        if s.handle == handle:
            current_user.sns.pop(i)
            db.session.delete(s)

    db.session.commit()

    return redirect(url_for('main.profile'))


@main.route('/profile', methods=['POST'])
@login_required
def follow_test():
    consumer_key = "OdgalfvMIxmDamj1S9TV6NbC0"

    consumer_secret = "0rS6CK5wg80USvR6X5PYQZHO3kdDDR0YP2PqYf8a7Nnz5JXaHH"

    access_token = "1269868735801602048-0iYCm7fzqpJfqAG8IMS5Yk1wBhiEzH"
    access_token_secret = "NvNBEM4nRwFEr2kwSNvtXVC87T7XDU1AEZmC5sCP4c7Vr"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    test = Site.query.all()

    for i in test:
        try:
            api.create_friendship(i)
        except:
            print("Couldn't follow account. //")

    return render_template('profile.html', user=current_user,
                           sns=current_user.sns)


app = create_app()

if __name__ == '__main__':
    db.create_all(app=create_app())  # create the SQLite database
    app.run(debug=True)  # run the flask app on debug mode
