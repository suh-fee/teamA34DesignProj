import pytest
import source.models, source.__init__, source.main

def f():
    raise SystemExit(1)

def bob():
    source.main.index()
    print("Index!")

def test_func():
    with pytest.raises(SystemExit):
        bob()
