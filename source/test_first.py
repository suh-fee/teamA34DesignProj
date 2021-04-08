import pytest
import source
from source import main


def bob():
    main.index()
    print("Index!")

def test_func():
    with pytest.raises(SystemExit):
        bob()
