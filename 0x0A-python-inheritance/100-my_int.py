#!/usr/bin/python3
"""Defining a class called MyInt"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __init__(self, val):
        """Instantiates object"""
        self.value = val

    def __ne__(self, var):
        """inverts the != operator"""
        return self.value == var

    def __eq__(self, var):
        """inverts the == operator"""
        return self.value != var
