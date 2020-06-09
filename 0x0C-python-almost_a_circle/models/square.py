#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """str"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id, self.x,
                                             self.y, self.width)

    @property
    def size(self):
        """getter"""
        return self.width

    @size.setter
    def size(self, value):
        """setter"""

        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update"""
        if args:
            a = ["id", "size", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, a[i], e)
            return

        for x, y in kwargs.items():
            if hasattr(self, x):
                setattr(self, x, y)

    def to_dictionary(self):
        """to dictionary"""

        n_dict = {}
        n_dict['id'] = self.id
        n_dict['size'] = self.width
        n_dict['x'] = self.x
        n_dict['y'] = self.y

        return n_dict
