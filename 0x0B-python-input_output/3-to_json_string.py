#!/usr/bin/python3
"""Defining a function called to_json_string"""
import json


def to_json_string(my_obj):
    """to_json_string function returns the JSON representation of
    an object (string).

    Args:
        my_obj: object
    """
    return json.dumps(my_obj)
