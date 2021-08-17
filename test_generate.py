import pytest

from generate import create_20array as c20
from generate import reshape2d as r

def test_smoke():
    assert 1+1==2

def test_create_20array():
    assert len(c20()) == 20

def test_r():
    assert len(r()) == 5