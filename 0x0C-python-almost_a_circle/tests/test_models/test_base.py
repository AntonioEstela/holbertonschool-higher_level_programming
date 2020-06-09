#!/usr/bin/python3


"""Test cases for the Base class"""


from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os.path
import unittest


class TestBase(unittest.TestCase):
    """TestBase class"""

    def setUp(self):
        """setUp method"""
        self.b1 = Base(12)
        self.b2 = Base()
        self.b3 = Base(65)
        self.b4 = Base()
        self.b5 = Base("str")
        self.b6 = Base(-4)

    def tearDown(self):
        """tearDown class"""
        if os.path.exists('Rectangle.json'):
            os.remove('Rectangle.json')

        if os.path.exists('Square.json'):
            os.remove('Square.json')

    def test_id(self):
        """test id"""
        self.assertEqual(self.b1.id, 12)
        self.assertEqual(self.b2.id, 1)
        self.assertEqual(self.b3.id, 65)
        self.assertEqual(self.b4.id, 2)
        self.assertEqual(self.b5.id, "str")
        self.assertEqual(self.b6.id, -4)
        self.b6.id = 5
        self.assertEqual(self.b6.id, 5)

    def test_to_json_string(self):
        """test json_to_string method"""
        dictionary = Rectangle(10, 7, 2, 8).to_dictionary()
        self.assertIsInstance(self.b1.to_json_string([dictionary]), str)
        self.assertIsNotNone(self.b1.to_json_string(None))
        self.assertEqual(self.b1.to_json_string(None), "[]")
        self.assertEqual(self.b1.__dict__, {"id": 12})
        self.assertEqual(str(type(self.b1)), "<class 'models.base.Base'>")

    def test_save_to_file(self):
        """test save_to_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        s1 = Square(4, 5, 6, 8)
        s2 = Square(7, 3, 11, 7)
        Rectangle.save_to_file([r1, r2])
        Square.save_to_file([s1, s2])

        self.assertTrue(os.path.exists('Rectangle.json'))
        self.assertTrue(os.path.exists('Square.json'))


if __name__ == "__main__":
    unittest.main()
