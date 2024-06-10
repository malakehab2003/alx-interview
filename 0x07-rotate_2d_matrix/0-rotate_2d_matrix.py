#!/usr/bin/python3
""" create rotate_2d_matrix function """


def rotate_2d_matrix(matrix):
    """ rotate 2d matrix clockwise """

    i = len(matrix) - 1
    j = 0
    new_matrix =[]
    while j < len(matrix[i]):
        new_row = []
        while i >= 0:
            new_row.append(matrix[i][j])
            i -= 1
        i = len(matrix) - 1
        j += 1
        new_matrix.append(new_row)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = new_matrix[i][j]
