#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    i = 0
    for x in new_matrix:
        new_matrix[i] = list(map(lambda x: x ** 2, x))
        i += 1
    return new_matrix
