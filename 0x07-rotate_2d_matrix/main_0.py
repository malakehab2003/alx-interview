#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

def print_matrix(matrix):
    """Helper function to print a 2D matrix in a readable format"""
    for row in matrix:
        print(row)

if __name__ == "__main__":
    # Test case 1: 3x3 matrix
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original matrix:")
    print_matrix(matrix1)
    rotate_2d_matrix(matrix1)
    print("Rotated matrix:")
    print_matrix(matrix1)
    print()

    # Test case 2: 4x4 matrix
    matrix2 = [
        [ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print("Original matrix:")
    print_matrix(matrix2)
    rotate_2d_matrix(matrix2)
    print("Rotated matrix:")
    print_matrix(matrix2)
    print()

    # Test case 3: 2x2 matrix
    matrix3 = [
        [1, 2],
        [3, 4]
    ]
    print("Original matrix:")
    print_matrix(matrix3)
    rotate_2d_matrix(matrix3)
    print("Rotated matrix:")
    print_matrix(matrix3)
    print()

    # Test case 4: 5x5 matrix
    matrix4 = [
        [ 1,  2,  3,  4,  5],
        [ 6,  7,  8,  9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    print("Original matrix:")
    print_matrix(matrix4)
    rotate_2d_matrix(matrix4)
    print("Rotated matrix:")
    print_matrix(matrix4)
    print()

    # Test case 5: 1x1 matrix
    matrix5 = [
        [1]
    ]
    print("Original matrix:")
    print_matrix(matrix5)
    rotate_2d_matrix(matrix5)
    print("Rotated matrix:")
    print_matrix(matrix5)
    print()
