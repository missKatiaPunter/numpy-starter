import pytest
import numpy as np

from matrix import mat_subset

a=np.arange(16).reshape(4,4)

def test_smoke():
    assert 1+1==2

def test_mat_subset():
    assert mat_subset([a]) == 9

