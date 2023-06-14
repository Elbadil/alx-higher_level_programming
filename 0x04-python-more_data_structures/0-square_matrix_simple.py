#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for lists in matrix:
        new_matrix.append(list(map(lambda x: x * x, lists)))
    return new_matrix
