#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""

Rectangle Class

"""


class Rectangle(BaseGeometry):
    """Rectangle Class"""

    def __init__(self, width, height):
        """Instantiation"""

        BaseGeometry.integer_validator("width", width)
        BaseGeometry.integer_validator("height", height)

        self.__width = width
        self.__height = height
