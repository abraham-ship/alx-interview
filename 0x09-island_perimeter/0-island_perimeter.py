#!/usr/bin/python3
'''Island Perimeter'''


def island_perimeter(grid):
    '''calculate perimeter of an island and
    return the perimeter of the island described in grid'''
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Assume all sides are land

                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 for shared edge

                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 for shared edge

    return perimeter
