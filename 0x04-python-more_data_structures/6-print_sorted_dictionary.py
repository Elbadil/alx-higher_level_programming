#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_sorted_dict = dict(sorted(a_dictionary.items()))
    for key, value in new_sorted_dict.items():
        print("{}: {}".format(key, value))
