#!/usr/bin/python3
""" Defining a function called text_indentation """


def text_indentation(text):
    """text_indentation function prints 2 new lines after each
    of these chars [".", "?", ":"] and removes spaces at the
    beginning or at the end of each printed line
    Args:
        text: the string to be printed in lines
    Raises:
        TypeError: if argument entered is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    idx = 0

    while idx < len(text) and text[idx] == " ":
        idx += 1

    while idx < len(text):
        print(text[idx], end="")
        if text[idx] in ["\n", ".", "?", ":"]:
            if text[idx] in [".", "?", ":"]:
                print("\n")
            idx += 1
            while idx < len(text) and text[idx] == " ":
                idx += 1
            continue
        idx += 1
