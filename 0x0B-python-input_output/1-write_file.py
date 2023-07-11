#!/usr/bin/python3
"""Defining a function called write_file"""


def write_file(filename="", text=""):
    """write_file function writes a string to a text file

    Args:
        filename: The name of the file to write on
        text: The text to be added to the file
    Returns:
        the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as File:
        return (File.write(text))
