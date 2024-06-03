#!/usr/bin/python3
"""
Solve N-Queens problem
"""

import sys

# Check the number of args
if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

# Check that the second arg is a number
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if number is less than 4
if n < 4:
    print('N must be at least 4')
    sys.exit(1)

def is_safe(board, row, col):
    """ Check if it's safe to place a queen at board[row][col] """
    
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col):
    """ Util function to solve N-Queens problem """
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1) or res
            board[i][col] = 0  # backtrack

    return res

def solve_nqueens():
    """ Solve N-Queens problem """
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_nqueens_util(board, 0):
        print("Solution does not exist")
        return False
    return True

solve_nqueens()
