#!/usr/bin/python3
"""Defining a function called pascal_triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal's triangle of n.

    Args:
        n: size of the triangle
    """
    if n <= 0:
        return []

    t_list = [[1]]

    for _ in range(n - 1):
        previous_row = t_list[-1]
        new_row = [1]

        for i in range(len(previous_row) - 1):
            sum_of_elements = previous_row[i] + previous_row[i + 1]
            new_row.append(sum_of_elements)

        new_row.append(1)
        t_list.append(new_row)

    return t_list
