#!/usr/bin/python3
"""wirte to a file"""


def append_write(filename="", text=""):
    """write to a file"""

    with open(filename, 'a') as f:
        char = f.write(text)

    return char
