#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for inner_list in matrix:
        numbers_joined = ' '.join(map(str, inner_list))
        print("{}".format(numbers_joined))
