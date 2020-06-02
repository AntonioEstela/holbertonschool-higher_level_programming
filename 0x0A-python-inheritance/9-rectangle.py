#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Rectangle Class"""


class Rectangle(BaseGeometry):
    """Rectangle Class"""

    def __init__(self, width, height):
        """Instantiation"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a description"""

        return "[{}] {}/{}".format(type(self).__name__, self.__width,
                                   self.__height)

    def area(self):
        """Method to calculate the area"""

        return self.__width * self.__height