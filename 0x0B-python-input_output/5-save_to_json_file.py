#!/usr/bin/python3
"""Defining a function called save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file function writes an Object to a text file,
    using a JSON representation.

    Args:
        my_obj: The object to write in a text file
        filename: The name of the file
    """
    with open(filename, "w", encoding="utf-8") as File:
        File.write(json.dumps(my_obj))
