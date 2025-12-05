#!/usr/bin/python3
"""Module for matrix_divided function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number.
    Args:
        matrix: List of lists of integers/floats
        div: Number to divide by (integer or float)
    Returns:
    New matrix with all elements divided by div, rounded to 2 decimal places
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows have different sizes,
                   or if div is not a number
        ZeroDivisionError: If div is 0
    """
    # Check if matrix is a list
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    # Check if all elements are integers or floats and rows have same size
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # Check if div is 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Divide all elements and round to 2 decimal places
    return [[round(element / div, 2) for element in row] for row in matrix]
