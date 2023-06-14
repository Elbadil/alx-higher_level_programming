#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    total_weight = 0
    weight_sum = 0

    for i in my_list:
        total_weight += i[0] * i[1]
        weight_sum += i[1]

    average = total_weight / weight_sum
    return average
