#!/usr/bin/python3
"""
Module for minimum operations
"""


def minOperations(n):
    """
    Computes fewest number of operations

    Returns:
        number of operation(int).
    """
    if not isinstance(n, int):
        return 0
    nb_of_ops = 0
    paste = 0
    increment = 1
    while increment < n:
        if paste == 0:
            paste = increment
            increment += paste
            nb_of_ops += 2
        elif n - increment > 0 and (n - increment) % increment == 0:
            paste = increment
            increment += paste
            nb_of_ops += 2
        elif paste > 0:
            # paste
            increment += paste
            nb_of_ops += 1
    return nb_of_ops
