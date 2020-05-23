#!/usr/bin/python3
"""
Function that prints My name is followed by:
<first name> and <last_name>
both of them should be a string, otherwhise a TypeError will raised
"""


def say_my_name(first_name, last_name=""):
    """Function that prints My name is followed by:
    <first name> and <last_name>
    both of them should be a string, otherwhise a TypeError will raised"""

    check = [first_name, last_name]

    if all(type(x) is str for x in check):
        print("My name is {} {}".format(first_name, last_name))

    elif isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")

    elif isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
