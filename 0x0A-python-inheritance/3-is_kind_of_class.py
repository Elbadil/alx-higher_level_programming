#!/usr/bin/python3
"""Defining a function called is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class returns True if the object is an instance of, 
    or if the object is an instance of a class that inherited from 
    the specified class, otherwise False.

    Args:
        obj: The object to check
        a_class: The class to check
    """
    return isinstance(obj, a_class)
