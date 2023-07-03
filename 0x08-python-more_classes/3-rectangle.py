#!/usr/bin/python3
"""Defining a Class called Rectangle"""


class Rectangle:
    """Class that defines a Rectangles width and height
    Methods:
        area: returns the rectangle area
        perimeter: returns the rectangle perimeter
        __str__: return a string to print the rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        rectangle_printed = ""
        if self.__height == 0 or self.__width == 0:
            return rectangle_printed

        for _ in range(self.__height - 1):
            rectangle_printed += "#" * self.__width + "\n"
        rectangle_printed += "#" * self.__width

        return rectangle_printed
