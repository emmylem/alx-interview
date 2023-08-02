#!/usr/bin/python3
"""Method that determines if all boxes can be Opened."""


def canUnlockAll(boxes):
    n = len(boxes)
    visited = set()
    """Start with box 0 as visited."""
    visited.add(0)
    stack = [0]

    while stack:
        currBox = stack.pop()
        for key in boxes[currBox]:
            if key not in visited:
                visited.add(key)
                stack.append(key)

    return len(visited) == n
