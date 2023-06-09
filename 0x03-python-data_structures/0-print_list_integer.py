#!/usr/bin/python3
def print_list_integer(my_list=[]):
    list_size = len(my_list) + 1
    for numbers in range(1, list_size):
        print("{}".format(numbers))
