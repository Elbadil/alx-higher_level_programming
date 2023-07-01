#!/usr/bin/python3
""" Defining a function called add_integer """


def add_integer(a, b=98):
    """ add_integer function returns the addition of two integers
    Args:
        a: first integer
        b: second integer
    Raises:
        TypeError if a parameter (a or b) are not floats or integers
    Returns:
        The addition of two integers (a, b)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
