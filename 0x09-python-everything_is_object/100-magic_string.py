#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "prnt", getattr(magic_string, "prnt", - 1) + 1)
    return "Holberton" + ", Holberton" * magic_string.prnt
