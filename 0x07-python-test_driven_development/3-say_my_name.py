#!/usr/bin/python3
""" Defining a function called say_my_name """


def say_my_name(first_name, last_name=""):
    """ say_my_name function prints the first and last name given
    Raises a TypeError if an argument is not a string
    Last name is optional the function will print first name
    regardless
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
