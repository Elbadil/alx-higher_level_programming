#!/usr/bin/python3
"""Defining class called LockedClass"""


class LockedClass:
    """prevents the user from dynamically creating new instance
    attributes except if the new instance attribute is called
    """
    __slots__ = ('first_name',)
