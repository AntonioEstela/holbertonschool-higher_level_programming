#!/usr/bin/python3
"""doc"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init"""
        super().__init__(size, size, x, y, id)

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
        """Update"""

        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.width = args[i]
            elif i == 2:
                self.height = args[i]
            elif i == 3:
                self.x = args[i]
            elif i == 4:
                self.y = args[i]

        if args is None or len(args) == 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.width = kwargs['size']
                self.height = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """to dictionary"""

        n_dict = {}
        n_dict['id'] = self.id
        n_dict['size'] = self.width
        n_dict['x'] = self.x
        n_dict['y'] = self.y

        return n_dict
