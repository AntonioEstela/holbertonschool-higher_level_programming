#!/usr/bin/python3
"""Function that returns the number of lines of a text file"""


def number_of_lines(filename=""):
    """Function that returns the number of lines of a text file"""
    with open(filename, "r") as f:
        return len(f.readlines())
