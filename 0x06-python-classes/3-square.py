#!/usr/bin/python3
"""Define a Class Called Square"""


class Square:
    """Represent a square with a private instance attribute
        size, takes only int as size and calculates area of a Square"""
    def __init__(self, size=0):
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
