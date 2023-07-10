#!/usr/bin/python3
"""Defining a class called MyList"""


class MyList(list):
    """Subclass of list with additional functionality"""

    def print_sorted(self):
        """print_sorted function that prints a list, but sorted"""
        new_list = sorted(self)
        print(new_list)
