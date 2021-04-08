import pytest
import source

def bob():
    source.main.index()
    print("Index!")

def test_func():
    with pytest.raises(SystemExit):
        bob()
