#!/usr/bin/python3
"""Define a Class Called Square"""


class Square:
    """Represent a square with a private instance attribute
        size and position """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(i, int) for i in value) and
                all(i >= 0 for i in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return
        i, j = self.__position
        for _ in range(j):
            print()
        for _ in range(self.__size):
            print(" " * i + self.__size * "#")
