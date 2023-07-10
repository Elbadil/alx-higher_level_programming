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
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
