#!/usr/bin/python3
"""Defining a function called is_same_class"""


def is_same_class(obj, a_class):
    """is_same_class function returns True if the object is exactly
    an instance of the specified class, otherwise False.

    Args:
        obj: The object to check
        a_class: The class to check
    """
    if type(obj) == a_class:
        return True
    return False
