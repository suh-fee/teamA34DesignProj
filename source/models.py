"""
This is the file containing all of the models that will be included in the
databases.
"""

from flask_login import UserMixin
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
    name = db.Column(db.String(1000))
    password = db.Column(db.String(100))
    sns = db.relationship('Site', backref='users') #db.backref('users',uselist=False))

    def avatar(self, size):
        """
        The purpose of this method is to create a profile image for each
        user's account.
        """
        #TODO: Allow users to upload their own profile image
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)


class Site(db.Model):
    __tablename__ = 'social_sites'
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(1000))
    handle = db.Column(db.String(1000))
    link = db.Column(db.String(1000))
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

