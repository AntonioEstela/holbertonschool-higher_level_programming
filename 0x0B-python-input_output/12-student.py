#!/usr/bin/python3
""" student class"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json"""
        if type(attrs) is list and all(isinstance(i, str) for i in attrs):
            nd = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    nd[k] = v
            return nd
        return self.__dict__
