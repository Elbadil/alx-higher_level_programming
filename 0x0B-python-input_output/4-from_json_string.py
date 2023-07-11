#!/usr/bin/python3
"""Defining a function called from_json_string"""
import json


def from_json_string(my_str):
    """from_json_string function returns an object (Python data structure)
    represented by a JSON string.

    Args:
        my_str: JSON string
    """
    return json.loads(my_str)
