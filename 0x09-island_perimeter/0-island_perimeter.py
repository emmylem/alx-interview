#!/usr/bin/python3
"""Island Perimeter Problem
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        the perimeter of the island
    """

    p = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Count the number of water neighbors.
                water_neighbors = 0
                if i == 0 or grid[i - 1][j] == 0:
                    water_neighbors += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    water_neighbors += 1
                if j == 0 or grid[i][j - 1] == 0:
                    water_neighbors += 1
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    water_neighbors += 1

                # Add the number of water neighbors to the perimeter.
                p += water_neighbors

    return p
