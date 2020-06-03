#!/usr/bin/python3
"""wirte to a file"""


def write_file(filename="", text=""):
    """write to a file"""

    with open(filename, 'w') as f:
        char = f.write(text)

    return char
