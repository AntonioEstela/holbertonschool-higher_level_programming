#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for x in range(len(new_matrix)):
        new_matrix[x] = list(map(lambda x: x ** 2, new_matrix[x]))
    return new_matrix
