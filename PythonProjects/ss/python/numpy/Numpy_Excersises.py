"""
Created on Aug 11, 2021

@author: Wyatt Meehan
"""

import numpy as np


def ten_zeros():
    return np.zeros(10)


def ten_ones():
    return np.ones(10)


def ten_fives():
    return np.ones(10) * 5


def ten_to_fifty():
    return np.arange(10, 51, 1)


def ten_to_fifty_even():
    return np.arange(10, 51, 2)


def three_by_three_matrix():
    return np.arange(0, 9).reshape(3, 3)


def identity_matrix():
    return np.identity(3)


def random():
    return np.random.random()


if __name__ == '__main__':
    print(ten_ones())
    print(ten_zeros())
    print(ten_fives())
    print(ten_to_fifty())
    print(ten_to_fifty_even())
    print(three_by_three_matrix())
    print(random())
