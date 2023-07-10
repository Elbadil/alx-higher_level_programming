#!/usr/bin/python3
"""Defining a class called BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """area method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
