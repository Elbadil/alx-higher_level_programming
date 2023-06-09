#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_cp = my_list.copy()
    if idx < 0:
        return list_cp
    if idx > len(my_list) - 1:
        return list_cp
    else:
        list_cp[idx] = element
    return list_cp
