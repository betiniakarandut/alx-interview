#!/usr/bin/python3
"""Module 0-rotate_2D_matrix.py"""

def rotate_2d_matrix(matrix):
    """Transpose of a matrix
    """
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # interchanging rows and columns
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]
