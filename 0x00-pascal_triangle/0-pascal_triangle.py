#!/usr/bin/python3
"""Module for Pascal triangle""" 


def pascal_triangle(n):
    """function to represent Pascal triangle

    Args:
        int(n)

    Returns:
        list representing pascal triangle
    """

    if n <= 0:
        return []
    trow = [1]
    y = [0]
    for x in range(max(n,0)):
        print(trow)
        trow=[l+r for l,r in zip(trow+y, y+trow)]
    return n

pascal_triangle(10)
