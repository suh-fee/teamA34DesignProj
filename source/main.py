"""
This is the file containining all of the non-auth routes for Flare app.
"""

from flask import Blueprint, render_template, redirect, url_for, request, abort, session
from flask_login import login_required, current_user
from source.__init__ import db, create_app
from source.models import User, Site
import tweepy

main = Blueprint('main', __name__)

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
    return render_template('profile.html', user=current_user,
                           sns=current_user.sns, handle=None, success=None)


@main.route('/add_site', methods=['GET'])
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

    # Update the database
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

    return render_template(template, user=user, sns=user.sns, success=None, handle=None)


@main.errorhandler(404)
def not_found(error):
    """
    The purpose of this function is to render a 404 page when a profile page
    for a given username does not exist.
    """
    return render_template('404.html'), 404


# Globals needed for twitter following: TODO find way to hide secret and key
callback_url = 'http://localhost:5000/follow_twitter2'
consumer_key = "OdgalfvMIxmDamj1S9TV6NbC0"
consumer_secret = "0rS6CK5wg80USvR6X5PYQZHO3kdDDR0YP2PqYf8a7Nnz5JXaHH"

testaccounts = ["@nimcanttweet", "@twitter"]


@main.route('/follow_twitter', methods=['GET', 'POST'])
@login_required
def follow_test():
    session['handle'] = request.form.get('twituser')
    print("TRYING", request.form.get('twituser'))

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_url)

    redirect_url = auth.get_authorization_url()

    session['request_token'] = auth.request_token

    return redirect(redirect_url)


@main.route('/follow_twitter2')
@login_required
def follow_twitter():
    """
    The purpose of this function is to integrate Twitter API functionality.
    It uses Tweepy to connect with the user's account and allows that user
    to follow another user's Twitter handle from within the Flare app.
    """
    success = None
    handle = None
    request_token = session['request_token']
    del session['request_token']
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_url)
    auth.request_token = request_token
    verifier = request.args.get('oauth_verifier')
    auth.get_access_token(verifier)
    auth.set_access_token(auth.access_token, auth.access_token_secret)
    api = tweepy.API(auth)

    try:
        api.create_friendship(session['handle'])
        success = "Followed Account!"
        handle = session['handle']
        success = True
    except:
        print("Could Not Follow Account:")
        print(session['handle'])

    return redirect(url_for('main.profile'))


if __name__ == '__main__':
    db.create_all(app=create_app())
    app.run(debug=True)
