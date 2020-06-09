#!/usr/bin/python3
"""Doc"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init"""
        my_dict = {'width': width, 'height': height, 'x': x, 'y': y}

        for k, v in my_dict.items():
            if type(v) is not int:
                raise TypeError("{} must be an integer".format(k))

        for k, v in {'x': x, 'y': y}.items():
            if v < 0:
                raise ValueError("{} must be >= 0".format(k))

        for k, v in {'width': width, 'height': height}.items():
            if v <= 0:
                raise ValueError("{} must be > 0".format(k))

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """str"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id, self.__x,
                                                self.__y, self.__width,
                                                self.__height)

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def display(self):
        """display method"""

        w, h = self.__width, self.__height

        print("\n" * self.__y, end="")
        for i in range(h):
            print(" " * self.__x, end="")
            for j in range(w):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """Update"""

        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.width = args[i]
            elif i == 2:
                print(args[i])
                self.height = args[i]
            elif i == 3:
                self.x = args[i]
            elif i == 4:
                self.y = args[i]

        if args is None or len(args) == 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """to dictionary"""

        n_dict = {}
        n_dict['id'] = self.id
        n_dict['width'] = self.width
        n_dict['height'] = self.height
        n_dict['x'] = self.x
        n_dict['y'] = self.y

        return n_dict
