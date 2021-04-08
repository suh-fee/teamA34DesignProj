import pytest

def f():
    raise SystemExit(1)

def test_func():
    with pytest.raises(SystemExit):
        f()
