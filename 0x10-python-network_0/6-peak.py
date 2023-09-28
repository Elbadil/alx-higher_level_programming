#!/usr/bin/python3
"""Defining a function find_peak"""


def find_peak(list_of_integers):
    """find_peak function that finds a peak in a list of 
    unsorted integers
    Args:
        list_of_integers: list to find the peak from
    """
    if len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    if len(list_of_integers) == 2:
        return max(list_of_integers)

    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = left + (right - left) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
