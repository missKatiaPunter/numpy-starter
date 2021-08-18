import pytest

from boolean import bool_array_use

def test_smoke():
    assert 1+1==2

def test_create_20array():
    assert bool_array_use([1,2,3,4,5,6]) == [2,4,6]

