#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary

    key_to_delete = []
    for key, val in a_dictionary.items():
        if val == value:
            key_to_delete.append(key)

    for key in key_to_delete:
        a_dictionary.pop(key)

    return a_dictionary
