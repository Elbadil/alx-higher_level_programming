#!/usr/bin/python3
"""Defining a function called lookup"""


def lookup(obj):
    """returns a list of available attributes and methods of an object
    Args:
        obj: object to get it's available attributes and methods
    """
    return dir(obj)
