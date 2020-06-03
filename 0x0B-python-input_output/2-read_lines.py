#!/usr/bin/python3
"""function that reads n lines of a text file and prints it to stdout"""


def read_lines(filename="", nb_lines=0):
    """function that reads n lines of a text file and prints it"""

    lines = len(open(filename).readlines())
    with open(filename, encoding="utf8") as f:
        if nb_lines > 0 and nb_lines < lines:
            for line in range(nb_lines):
                print(f.readline(), end="")
        else:
            print(f.read(), end="")
