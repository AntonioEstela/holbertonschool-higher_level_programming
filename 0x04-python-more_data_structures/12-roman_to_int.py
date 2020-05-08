#!/usr/bin/python3
def roman_to_int(roman_string):
    check = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    if type(roman_string) is not str or roman_string == 0:
        return 0

    for i in range(len(roman_string)):
        if i == 0 or check[roman_string[i]] <= check[roman_string[i - 1]]:
            num += check[roman_string[i]]
        else:
            num += check[roman_string[i]] - 2 * check[roman_string[i - 1]]

    return num
