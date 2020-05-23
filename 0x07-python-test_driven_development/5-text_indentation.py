#!/usr/bin/python3
"""
Function that prints a text with 2 new lines after the folowwing characters
Characters to split: ":", "?", "."
Parameters: text must be a string otherwhise an error will raised.
"""


def text_indentation(text):
    """Function that prints a text with 2 new lines after the folowwing characters
    Characters to split: ":", "?", "."
    Parameters: text must be a string otherwhise an error will raised."""

    delimiters = [".", ":", "?"]
    i = 0

    if type(text) is str and len(text) >= 0:
        length = len(text)
        while i < length:
            print(text[i], end="")
            if text[i] in delimiters:
                print("\n")
                try:
                    if text[i + 1] == " ":
                        while text[i + 1] == " ":
                            i += 1
                except Exception:
                    pass
            i += 1

    else:
        raise TypeError("text must be a string")
