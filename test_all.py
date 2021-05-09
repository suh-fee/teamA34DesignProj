import os
import tempfile

import pytest

import source.__init__ as sinit



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

def test_get_homepage(client):
    rv = client.get('/')
    assert b'Welcome to Flare!' in rv.data
    assert b'A site to link all your Social Media accounts.' in rv.data

def test_get_signup(client):
    rv = client.get('/signup')
    assert b'Sign Up' in rv.data

def test_post_signup(client):
    rv = client.post('/signup', data=dict(
        email = "test@test.com",
        name = "testName",
        password = "testPassword"
    ), follow_redirects=True)
    assert b'Login' in rv.data

def test_get_login(client):
    rv = client.get('/login')
    assert b'Login' in rv.data

def test_post_login(client):
    rv = client.post('/login', data=dict(
        email = "test@test.com",
        name = "testName",
        password = "testPassword"
    ), follow_redirects=True)
    assert b'Linked Accounts' in rv.data



