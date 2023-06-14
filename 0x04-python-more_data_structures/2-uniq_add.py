#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    uniq_list = set(my_list)
    for number in uniq_list:
        result += number
    return result
