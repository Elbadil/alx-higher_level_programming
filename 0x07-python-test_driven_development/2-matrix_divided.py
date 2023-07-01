#!/usr/bin/python3
""" Defining a function called matrix_divided """


def matrix_divided(matrix, div):
    """
    matrix_divided function returns a new matrix with all elements
    divided by div(div can be an integer or a float).
    Raises a TypeError if
    - div is zero
    - div not a float or integer
    - Elements of the matrix are not floats or integers
    - Lists of the matrix do not have the same size
    """
    if not isinstance(matrix, list) or not\
       all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = len(matrix[0])
    divided_new_mtrx = []

    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        else:
            divided_row = []

        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            else:
                divided_row.append(round(col / div, 2))
        divided_new_mtrx.append(divided_row)
    return divided_new_mtrx
