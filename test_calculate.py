import pytest

import calculate as c

def test_add():
    assert c.add_arrays([2,2],[3,3]) == [5,5]

