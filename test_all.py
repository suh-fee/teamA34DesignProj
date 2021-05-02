import os
import tempfile

import pytest

import source.__init__ as sinit
from source import models



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
    """Start with a blank database."""
    rv = client.get('/')
    assert rv.data != None

def test_getting_login(client):
    """Start with a blank database."""
    rv = client.get('/profile')
    assert rv.data != None

def test_getting_add_site(client):
    """Start with a blank database."""
    rv = client.get('/add_site')
    assert rv.data != None



