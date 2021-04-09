import pytest

def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    print("got here!")
    assert b'No entries here so far' in rv.data
