"""
This is the file containining all of the non-auth routes for Flare app.
"""

from flask import Blueprint, render_template, redirect, url_for, request, abort
from flask_login import login_required, current_user
from source.__init__ import db, create_app
from source.models import Site, User

import tweepy

main = Blueprint('main', __name__)

testaccounts = ["@nimcanttweet", "@twitter"]

app = create_app()


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


@main.route('/search')
def search():
    """
    The purpose of this function is to render the site that allows users to
    search for other users' profiles.
    """
    return render_template('search.html')


@main.route('/search', methods=['POST'])
def search_post():
    """
    The purpose of this function is to obtain the username a user wants to
    search for. This information is sent through an HTML POST request and
    is captured and redirected to the show_user function.
    """
    username = request.form.get('username')

    return redirect(url_for('main.show_user', username=username))


@main.route('/user/<username>')
def show_user(username=None):
    """
        The purpose of this function is to allow non-registered and registered
        users to view another user's profile. It searches for the <username>
        in the database and renders the profile. If the usernae does not exist,
        it returns a 404 error.
    """
    if username and (current_user.is_anonymous or username != current_user.name):
        user = User.query.filter_by(name=username).first()
        if user is None:
            abort(404)
    else:
        user = current_user
    if username:
        template = 'profile.html'

    return render_template(template, user=user, sns=user.sns)


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
        except Exception:
            print("Couldn't follow account. //")

    return render_template('profile.html', user=current_user,
                           sns=current_user.sns)


@main.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    db.create_all(app=create_app())  # create the SQLite database
    app.run(debug=True)  # run the flask app on debug mode
