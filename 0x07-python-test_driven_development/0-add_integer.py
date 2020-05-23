#!/usr/bin/python3
"""
Function that returns the addition of 2 integers.
Parameters: a and b.
a and b must be and integers or floats otherwhise a TypeError will raised.
"""


def add_integer(a, b=98):
    """Function that returns the addition of 2 integers.
       Parameters: a and b must be and integers or floats
       otherwhise a TypeError will raised."""

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    if a is None:
        a = 0

    if b is None:
        b = 0

    return a + b
