#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """class Rectangle that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Instantation"""

        self.height = height
        self.width = width

    @property
    def width(self):
        """Property to get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting a new value for width"""

        self.__width = value

        if type(self.__width) is not int:
            raise TypeError("width must be an integer")

        if self.__width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Property to get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting a new value for height"""

        self.__height = value

        if type(self.__height) is not int:
            raise TypeError("height must be an integer")

        if self.__height < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Method to calculate the area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Method to calculate the perimeter of the rectangle"""

        if any(check is 0 for check in [self.__height, self.__width]):
            return 0

        else:
            return (self.__width * 2) + (self.__height * 2)
