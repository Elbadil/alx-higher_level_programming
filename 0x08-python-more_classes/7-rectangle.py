#!/usr/bin/python3
"""Defining a Class called Rectangle"""


class Rectangle:
    """Class that defines a Rectangles width and height
    Methods:
        area: returns the rectangle area
        perimeter: returns the rectangle perimeter
        __str__: returns a string to print the rectangle
        __repr__: returns a string representation of an object
        __del__: prints a message when an instance of Rectangle is deleted
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        printed = ""
        if self.__height == 0 or self.__width == 0:
            return printed

        for _ in range(self.__height - 1):
            printed += str(self.print_symbol) * self.__width + "\n"
        printed += str(self.print_symbol) * self.__width

        return printed

    def __repr__(self) -> str:
        """Returns a string representation of an object"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
