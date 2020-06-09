#!/usr/bin/python3
"""Base Class"""
import json
import os.path


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes instances"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json_to_string"""

        if list_dictionaries is None:
            list_dictionaries = []

        list_dictionaries = json.dumps(list_dictionaries)
        return str(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        list_o = []
        if list_objs is not None:
            for i in list_objs:
                list_o.append(cls.to_dictionary(i))

        with open('{}.json'.format(cls.__name__), 'w') as f:
            f.write(cls.to_json_string(list_o))

    @staticmethod
    def from_json_string(json_string):
        """form json string"""

        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create"""

        if cls.__name__ == 'Rectangle':
            from models.rectangle import Rectangle
            obj = Rectangle(1, 1)
            obj.update(**dictionary)

        elif cls.__name__ == 'Square':
            from models.square import Square
            obj = Square(1)
            obj.update(**dictionary)

        return obj

    @classmethod
    def load_from_file(cls):
        """load_from_file"""
        a = []
        if os.path.exists('./{}.json'.format(cls.__name__)):
            with open('{}.json'.format(cls.__name__), 'r') as f:
                return [cls.create(**i) for i in
                        cls.from_json_string(f.read())]
        else:
            return a
