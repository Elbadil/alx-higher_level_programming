#!/usr/bin/python3
"""Define a Class Called Square"""


class Square:
    """Represent a square with a private instance attribute
        size, takes only int as size, defines property and property setter
        for size and calculates area of a Square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        counter = self.__size
        if self.__size == 0:
            print()
        while counter > 0:
            print(self.__size * "#")
            counter -= 1
