#!/usr/bin/python3
"""Module for 0-island_perimeter.py"""


def island_perimeter(grid):
    """Calculate the perimeter of an island in grid

    Arg:
        grid(list[int])

    returns:
        perimeter of island
    """
    if len(grid) == 0:
        return
    row = len(grid)
    col = len(grid[0])
    perimeter = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                perimeter += 4
                # check neighbours(top, bottom, left, and right)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    # subtract 2 from shared edge(i.e neighbors)
                    perimeter -= 2
    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
