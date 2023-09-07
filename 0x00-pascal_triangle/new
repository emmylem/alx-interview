#!/usr/bin/python3
"""Pascal's Triangle."""


def pascal_triangle(n):
    """Creating a function that returns
    list of integers."""
    ret = []
    if (n <= 0):
        return ret
    new = ret.append([1])
    for i in range(n - 1):
        new + [ret[i][j] + ret[i][j + 1]
               for j in range(len(ret[i] - 1)] + [1])
    return ret
