#!/usr/bin/python3
""" create island_perimeter function """


def check_surrounded(grid, i, j):
    """ check the island surrounding is water or not """
    perimeter = 0
    if i == 0:
        perimeter += 1
    elif grid[i - 1][j] == 0:
        perimeter += 1
    if i == len(grid) - 1:
        perimeter += 1
    elif grid[i + 1][j] == 0:
        perimeter += 1
    if j == 0:
        perimeter += 1
    elif grid[i][j - 1] == 0:
        perimeter += 1
    if j == len(grid[i]) - 1:
        perimeter += 1
    elif grid[i][j + 1] == 0:
        perimeter += 1

    return perimeter


def island_perimeter(grid):
    """ calculate perimeter of island as grid """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                continue
            else:
                perimeter += check_surrounded(grid, i, j)

    return perimeter
