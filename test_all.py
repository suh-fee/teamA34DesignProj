import os
import tempfile

import pytest

import source.__init__ as sinit


'''This function is used to set up the client'''
@pytest.fixture
def client():
    app = sinit.create_app()
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            sinit.db.create_all()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

'''This function is used to login the dummy user that was created 
in the test_post_sign_up function, so the internal pages that require 
an account to view can be viewed'''
def login(client):
    rv = client.post('/login', data=dict(
        email="test@test.com",
        name="testName",
        password="testPassword"
    ), follow_redirects=True)
    return rv

'''This function is used to add a dummy site, 
so the internal pages that require a site added in the account
can be tested (like removing a site)'''
def add_site(client):
    rv = client.post('/add_site', data=dict(
        site="YouTube",
        handle="PewDiePie",
        link="https://www.youtube.com/user/PewDiePie"
    ), follow_redirects=True)
    return rv


def test_get_homepage(client):
    rv = client.get('/')
    assert b'Welcome to Flare!' in rv.data

def test_get_signup(client):
    rv = client.get('/signup')
    assert b'Sign Up' in rv.data

def test_post_signup(client):
    rv = client.post('/signup', data=dict(
        email = "test@test.com",
        username = "testName",
        password1 = "testPassword"
        password2 = "testPassword"
    ), follow_redirects=True)
    assert b'Login' in rv.data

def test_get_login(client):
    rv = client.get('/login')
    assert b'Login' in rv.data

def test_post_login(client):
    rv = login(client)
    assert b'Linked Accounts' in rv.data

def test_get_logout(client):
    login(client)
    rv = client.get('/logout', follow_redirects=True)
    assert b'Welcome to Flare!' in rv.data

def test_get_homepage_ater_login(client):
    login(client)
    rv = client.get('/')
    assert b'Welcome to Flare' in rv.data

def test_get_settings(client):
    login(client)
    rv = client.get('/settings')
    assert b'Link a New Account' in rv.data

def test_get_profie(client):
    login(client)
    rv = client.get('/profile')
    assert b'Linked Accounts' in rv.data

def test_get_add_site(client):
    login(client)
    rv = client.get('/add_site')
    assert b'Link Your Account To A Social Networking Site' in rv.data

def test_post_add_site(client):
    login(client)
    rv = client.post('/add_site', data=dict(
        site="YouTube",
        handle="PewDiePie",
        link="https://www.youtube.com/user/PewDiePie"
    ), follow_redirects=True)
    assert b'Linked Accounts' in rv.data


def test_get_remove_site(client):
    login(client)
    rv = client.get('/remove_site')
    assert b'Unlink A Social Networking Site From Your Account' in rv.data

def test_post_remove_site(client):
    login(client)
    add_site(client)
    rv = client.post('/remove_site', data=dict(
        handle="PewDiePie"
    ), follow_redirects=True)
    assert b'Linked Accounts' in rv.data

def test_get_search(client):
    login(client)
    rv = client.get('/search')
    assert b'Type a Username to Visit Their Profile' in rv.data

def test_post_search(client):
    rv = client.post('/search', data=dict(
        username="testName",
    ), follow_redirects=True)
    assert b"testName's Profile" in rv.data

def test_get_show_user(client):
    login(client)
    rv = client.get('/user/testName')
    assert b"testName's Profile" in rv.data