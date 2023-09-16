import pytest

def inc(x):
    return x+1

def test_answer():
    assert inc(3)==5

def test_wrong_answer():
    assert not inc(3)==5