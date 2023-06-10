#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    list_size = len(my_list) - 1
    for num in range(list_size):
        if idx >= 0 and num == idx:
            del my_list[num]
    return my_list
