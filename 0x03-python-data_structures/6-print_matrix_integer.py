#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for in_list in matrix:
        for number in in_list:
            if number != in_list[-1]:
                print("{:d} ".format(number), end='')
            else:
                print("{:d}".format(number), end='')
        print()
