#!/usr/bin/python3
"""read_file"""


def read_file(filename=""):
    """function that reads a text file"""
    with open(filename, "r", encoding="utf8") as f:
        print(f.read(), end="")
