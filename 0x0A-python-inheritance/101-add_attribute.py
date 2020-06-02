#!/usr/bin/python3
def add_attribute(obj, att, val):
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, att, val)
