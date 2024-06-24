#!/usr/bin/python3
""" create island_perimeter function """


def check_surrounded(grid, i, j):
    """ check the island surrounding is water or not """
    perimeter = 0
    if grid[i - 1][j] == 0:
        perimeter += 1
    if grid[i + 1][j] == 0:
        perimeter += 1
    if grid[i][j - 1] == 0:
        perimeter += 1
    if grid[i][j + 1] == 0:
        perimeter += 1

    return perimeter


def island_perimeter(grid):
    """ calculate perimeter of island as grid """
    perimeter = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] == 0:
                continue
            else:
                perimeter += check_surrounded(grid, i, j)

    return perimeter
