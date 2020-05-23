#!/usr/bin/python3
"""
Function that prints a square with the caracter #.
Parameters: the size of the square to print.
The size should be a integer greater than 0 otherwhise an error will raised
"""


def print_square(size):
    """Function that prints a square with the caracter #.
    Parameters: the size of the square to print.
    The size should be a integer greater than 0
    otherwhise an error will raised."""

    if type(size) is int:
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            for i in range(size):
                for j in range(size):
                    print("#", end="")
                print("")
    else:
        raise TypeError("size must be an integer")
