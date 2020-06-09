"""Testing Rectangle class"""


import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """ Suite to test Rectangle class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """ Test new rectangle """

        new = Rectangle(1, 1)
        new2 = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.width, 2)
        self.assertEqual(new2.height, 3)
        self.assertEqual(new2.x, 4)
        self.assertEqual(new2.y, 5)
        self.assertEqual(new2.id, 6)

    def test_new_rectangle_2(self):
        """ Test new rectangles """

        new = Rectangle(1, 1)
        new2 = Rectangle(1, 1)
        self.assertFalse(new is new2)
        self.assertFalse(new.id == new2.id)

    def test_is_Base_instance(self):
        """ Test Rectangle is a Base instance """

        new = Rectangle(1, 1)
        self.assertIsInstance(new, Base)

    def test_access_private_attrs(self):
        """ Trying to access to a private attribute """

        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__width

        with self.assertRaises(AttributeError):
            new.__height

        with self.assertRaises(AttributeError):
            new.__x

        new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            new.__y

    def test_incorrect_amount_attrs(self):
        """test incorrect_amount_attrs"""

        with self.assertRaises(TypeError):
            new = Rectangle(1)

        with self.assertRaises(TypeError):
            new = Rectangle()

    def test_valide_attrs(self):
        """ Trying to pass a string value """

        with self.assertRaises(TypeError):
            new = Rectangle("2", 2, 2, 2, 2)

        with self.assertRaises(TypeError):
            new = Rectangle(2, "2", 2, 2, 2)

        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, "2", 2, 2)

        with self.assertRaises(TypeError):
            new = Rectangle(2, 2, 2, "2", 2)

    def test_value_attrs(self):
        """ Trying to pass invalid values """

        with self.assertRaises(ValueError):
            new = Rectangle(0, 1)

        with self.assertRaises(ValueError):
            new = Rectangle(1, 0)

        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, -1)

        with self.assertRaises(ValueError):
            new = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """ Checking the return value of area method """

        new = Rectangle(4, 5)
        self.assertEqual(new.area(), 20)
        new.width = 5
        self.assertEqual(new.area(), 25)
        new.height = 5
        self.assertEqual(new.area(), 25)

    def test_display(self):
        """ Test string printed """

        r1 = Rectangle(2, 5)
        res = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
        """ Test string printed """

        r1 = Rectangle(5, 4, 1, 1)
        res = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """ Test __str__ return value """
        r1 = Rectangle(3, 3)
        res = "[Rectangle] (1) 0/0 - 3/3"
        self.assertEqual(r1.__str__(), res)

    def test_to_dictionary(self):
        """ Test dictionary returned """

        r1 = Rectangle(1, 2, 3, 4, 1)
        res = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_dict_to_json(self):
        """ Test Dictionary to JSON string """

        r1 = Rectangle(2, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_check_value(self):
        """ Test args passed """

        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)

        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)

    def test_create_5(self):
        """ Test create method """

        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
