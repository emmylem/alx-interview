#!/usr/bin/python3
"""Calculating Minimum number of operations."""


def minOperations(n):
    if n == 1:
        return 0
    
    operations = [0] * (n + 1)
    
    for i in range(2, n + 1):
        for j in range(i // 2, 0, -1):
            if i % j == 0:
                operations[i] = operations[j] + (i // j)
                break
    
    return operations[n]
