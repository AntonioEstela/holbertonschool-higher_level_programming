#!/usr/bin/python3
def add_attribute(obj, att, val):
    if hasattr(obj, '__dict__') is True:
        setattr(obj, att, val)
    else:
        raise TypeError('can\'t add new attribute')
