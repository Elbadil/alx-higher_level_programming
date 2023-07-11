#!/usr/bin/python3
"""Defining a function called load_from_json_file"""
import json


def load_from_json_file(filename):
    """load_from_json_file function creates an Object from a
    “JSON file”.

    Args:
        filename: the name of the JSON file
    """
    with open(filename, 'r', encoding="utf-8") as JsonFile:
        return json.load(JsonFile)
