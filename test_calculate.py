import pytest

import calculate as c

def test_add():
    assert c.add_arrays([2,2],[3,3]) == [5,5]

def test_multiply():
    all([a == b for a, b in zip(c.multiply_two_arrays([2,2],[2,2]), [4,4])])

def test_subtract_two_arrays():
    all([a == b for a, b in zip(c.subtract_two_arrays([2,2],[1,1]), [1,1])])


def test_divide_two_arrays():
    all([a == b for a, b in zip(c.divide_two_arrays([2,2],[1,1]), [1,1])])