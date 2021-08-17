import pytest

from generate import create_20array as c20

def test_smoke():
    assert 1+1==2

def test_create_20array():
    assert len(c20()) == 20