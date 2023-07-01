#!/usr/bin/python3
""" Defining a function called print_square """


def print_square(size):
    """print_square function prints a square using "#"
    Args:
        size: size of the square
    Raises:
        TypeError is the size is not an integer
        ValueError if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
