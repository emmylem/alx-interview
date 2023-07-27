#!/usr/bin/python3
"""Pascal's Triangle."""


def pascal_triangle(n):
    """Creating a function that returns
    list of integers."""
    ret = []
    if (n > 0):
        for i in range(1, n + 1):
            new = []
            x = i
            for j in range(1, i + 1):
                new.append(x)
                x = x * (i - j) // j
            ret.append(new)
    return ret
