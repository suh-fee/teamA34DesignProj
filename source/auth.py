"""
This file contains all auth routes for Flare
"""

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from __init__ import db
from models import User

auth = Blueprint('auth', __name__)


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # Check if the query returns a User
    # This means a user with this email already exists in the Database
    user = User.query.filter_by(email=email).first()

    # If a user is found, flash a warning
    # Reload the Sign Up page to try again
    if user:
        flash("An account associated with this email address already exists")
        return redirect(url_for('auth.signup'))

    # Create a new user from the data provided
    # Password is hashed before saving
    new_user = User(email=email, name=name,
                    password=generate_password_hash(password, method='sha256'))

    # Update the Database to include the new user
    db.session.add(new_user)
    db.session.commit()

    # Redirect the user to the Login page
    return redirect(url_for('auth.login'))


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # Check if the User already exists
    # Hash the password and see if it matches password in DB
    if not user or not check_password_hash(user.password, password):
        flash('Wrong login details. Please try again.')
        # Reload the Login page to try again
        return redirect(url_for('auth.login'))

    # If credentials are ok, redirect to main profile
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/settings')
@login_required
def settings():
    # TODO: create a settings html
    return render_template('settings.html')