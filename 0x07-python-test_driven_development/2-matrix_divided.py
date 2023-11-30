#!/usr/bin/python3
"""
my task
"""

def matrix_divided(matrix, div):
    """
    Divide a matrix of values by a single divisor.

    Args:
        matrix (list of lists of ints or floats): 2D list to operate on
        div (int or float): divisor for members of matrix

    Returns:
        list of lists of floats: New matrix with quotients for each member
                                of the original matrix divided by div
    """
    new_matrix = []

    # Check if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    for row in matrix:
        # Check if each element is a list
        if not isinstance(row, list):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

        # Check if each row of the matrix has the same size
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')

        # Check if each element in the row is an integer or float
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')

    # Divide all elements of the matrix by div, rounded to 2 decimal places
    for row in matrix:
        new_row = [round(value / div, 2) for value in row]
        new_matrix.append(new_row)

    return new_matrix

