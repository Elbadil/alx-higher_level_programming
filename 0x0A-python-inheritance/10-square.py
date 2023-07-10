#!/usr/bin/python3
"""Defining a class called Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle."""

    def __init__(self, size):
        """Intialize a new Square.

        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
