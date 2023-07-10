#!/usr/bin/python3
"""Defining a class called BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """area method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator method that validates value.

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
