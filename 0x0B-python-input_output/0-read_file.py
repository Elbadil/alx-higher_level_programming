#!/usr/bin/python3
"""Defining a function called read_file"""


def read_file(filename=""):
    """read_file function opens a file and read it's content

    Args:
        filename: the file to be read
    """
    with open(filename, "r", encoding="utf-8") as File:
        print(File.read(), end="")
