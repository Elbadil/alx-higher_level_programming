#!/usr/bin/python3
"""Defining a class called BaseGeometry"""


class BaseGeometry:
    """Class Basegeometry."""

    def area(self):
        """area function not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator function checks if value is an integer.

        Args:
            name: The name of the parameter.
            value: The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width: The width of the new Rectangle.
            height: The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area function returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of the method area"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Class Square that inherits from Rectangle."""

    def __init__(self, size):
        """Intialize a new Square.

        Args:
            size: size of the square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area function returns the area of a Square"""
        return self.__size ** 2
