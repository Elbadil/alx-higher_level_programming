#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_cp = []
    for num in my_list:
        if num % 2 == 0:
            list_cp.append(True)
        else:
            list_cp.append(False)
    return list_cp
