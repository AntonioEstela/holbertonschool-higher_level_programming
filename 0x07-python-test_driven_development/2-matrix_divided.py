#!/usr/bin/python3
"""

Function that divides all the elements of a matrix

"""


def matrix_divided(matrix, div):
    """Function that divides all the elements of a matrix"""
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if matrix is None or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    first_len = len(matrix[0])

    for check in matrix:
        if len(check) is not first_len:
            raise TypeError('Each row of the matrix must have the same size')
        if len(check) == 0 or any(type(num) is not int and
                                  type(num) is not float for num in check):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(list(map(lambda x: round(x / div, 2), matrix[i])))

    return new_matrix
