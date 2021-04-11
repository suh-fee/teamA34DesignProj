import os
import tempfile

import pytest

import source
import source.__init__ as sinit

'''
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

def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert rv.data != None'''
