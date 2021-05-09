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

def test_getting_homepage(client):
    rv = client.get('/')
    assert b'Welcome to Flare!' in rv.data
    assert b'A site to link all your Social Media accounts.' in rv.data

def test_getting_login(client):
    rv = client.get('/login')
    assert b'Login' in rv.data

def test_getting_signup(client):
    rv = client.get('/signup')
    assert b'Sign Up' in rv.data
