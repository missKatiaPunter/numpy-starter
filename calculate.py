# Add more functions to the module calculate. Try adding, subtracting, dividing np.arrays

import numpy as np

def add_arrays(list1, list2):
    np_1 = np.array(list1)
    np_2 = np.array(list2)
    return list(np_1+np_2)

# You will get the bug here: convert returned val into a list

def multiply_by_num(list1, num):
    return np.array(list1)*num