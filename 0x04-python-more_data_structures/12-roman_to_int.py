#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return None

    result = 0
    for i in range(len(roman_string)):
        if i < len(roman_string) - 1:
            if roman_string[i] == 'I' and roman_string[i + 1] in ['X', 'V']:
                result -= 2
        if roman_string[i] == 'I':
            result += 1
        if roman_string[i] == 'V':
            result += 5
        if roman_string[i] == 'X':
            result += 10
        if roman_string[i] == 'L':
            result += 50
        if roman_string[i] == 'C':
            result += 100
        if roman_string[i] == 'D':
            result += 500
        if roman_string[i] == 'M':
            result += 1000

    return result
