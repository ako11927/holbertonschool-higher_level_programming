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
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    
    # Check if each row is a list and has the same size
    row_size = None
    for i, row in enumerate(matrix):
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        
        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        
        # Check if all elements in row are integers or floats
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
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            # Round to 2 decimal places
            result = round(element / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)
    
    return new_matrix
