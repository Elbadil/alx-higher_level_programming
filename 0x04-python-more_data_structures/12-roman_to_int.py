#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return None

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
    result = 0

    for i in range(len(roman_string)):
        if roman_string[i] not in roman_dict.keys():
            return None

        roman_value = roman_dict[roman_string[i]]
        if i < len(roman_string) - 1:
            if roman_string[i] == 'I' and roman_string[i + 1] in ['X', 'V']:
                result -= 2

        result += roman_value

    return result
