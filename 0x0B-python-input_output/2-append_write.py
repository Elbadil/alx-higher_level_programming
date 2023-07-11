#!/usr/bin/python3
"""Defining a function called append_write"""


def append_write(filename="", text=""):
    """append_write function appends a string at the end
    of a text file.

    Args:
        filename: The name of the file to write on
        text: The text to be appended to the file
    Returns:
        the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as File:
        return (File.write(text))
