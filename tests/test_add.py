# test_add.py
from acnaweblib import add


def test_result_ok():
    assert add(1,2) == 3


def test_result_wrong():
    assert add(5,2) != 3    
