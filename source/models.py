"""
This is the file containing all of the models that will be included in the
databases.
"""

from flask_login import LoginManager, UserMixin
from hashlib import md5
from source.__init__ import db


class User(db.Model, UserMixin):
    """
    The purpose of this class is to create the fields for the User database,
    including all of the information that is captured from a user upon signup.
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(1000), unique=True)
    password = db.Column(db.String(100))
    sns = db.relationship('Site', backref='users')

    def avatar(self, size):
        """
        The purpose of this method is to generate a random profile image for
        each user's account using Gravatar.
        """
        # TODO: Allow users to upload their own profile image
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)


class Site(db.Model):
    """
    The purpose of this class is to create the fields for the Site database,
    including all of the information that is captured when a user links a new
    site to their account.
    """
    __tablename__ = 'social_sites'
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(1000))
    handle = db.Column(db.String(1000))
    link = db.Column(db.String(1000))
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))


def manage_login(app):
    """
    The purpose of this function is to set up Flask's LoginManager. It defines
    the function that allows us to query the database to retriever User
    information.
    """
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
