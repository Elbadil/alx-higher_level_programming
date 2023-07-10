#!/usr/bin/python3
"""Defining a function called inherits_from"""


def inherits_from(obj, a_class):
    """inherits_from function returns True if the object is an
    instance of a class that inherited (directly or indirectly)
    from the specified class, otherwise False.

    Args:
        obj: The object to check
        a_class: The class to check
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
