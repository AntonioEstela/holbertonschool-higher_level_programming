#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Instantation"""

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Property to get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting a new value for width"""

        self.__width = value

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Property to get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting a new value for height"""

        self.__height = value

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")