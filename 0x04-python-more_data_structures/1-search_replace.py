#!/usr/bin/python3
def search_replace(my_list, search, replace):
    rplced_list = my_list.copy()
    for i in range(len(my_list)):
        if rplced_list[i] == search:
            rplced_list[i] = replace
    return rplced_list
