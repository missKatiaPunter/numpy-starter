# Create another function that generates a 1d array of 99
# Reshape into 2d using shapable params

import numpy as np

def create_20array():
    return np.arange(1, 21)

def reshape2d():
    return create_20array().reshape(5,4)

print(reshape2d())