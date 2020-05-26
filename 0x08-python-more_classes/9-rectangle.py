#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """class Rectangle that defines a rectangle"""

    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instantation"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __repr__(self):
        """“official” string representation of a Rectangle class"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __str__(self):
        """“informal” string representation of a Rectangle class"""

        ret_str = ""
        if all(check is not 0 for check in [self.__width, self.__height]):
            for h in range(self.__height):
                for w in range(self.__width):
                    ret_str += str(self.print_symbol)
                ret_str += "\n"

        return ret_str[:-1]

    @property
    def width(self):
        """Property to get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting a new value for width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Property to get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting a new value for height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Method to calculate the area of the rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """Method to calculate the perimeter of the rectangle"""

        if any(check is 0 for check in [self.__height, self.__width]):
            return 0

        else:
            return (self.__width * 2) + (self.__height * 2)

    def __del__(self):
        """Method to print something when the instance of a class is
        garbage colection"""

        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the biggestrectangle based on the area
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() < rect_1.area():
            return rect_1

        if rect_1.area() == rect_2.area():
            return rect_1

        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method that returns a new Rectangle instance"""

        return cls(size, size)
