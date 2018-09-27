#!/usr/bin/env python3

import unittest
from collections import namedtuple


class TestTuples(unittest.TestCase):

    def test_types(self):
        # tuple
        self.assertEqual(type((1, 'a')), tuple)

        # namedtuple
        # https://stackoverflow.com/questions/2970608/what-are-named-tuples-in-python#2970722
        Point = namedtuple('Point', 'x, y')
        my_point = Point(3, 5)
        self.assertEqual(type(my_point), Point)
        self.assertEqual(my_point.x, 3)
        self.assertEqual(my_point.y, 5)

    def test_tuple_slice(self):
        """
        slice works on tuple similar to list
        """
        my_tuple = ('a', 'b', 'c')
        self.assertEqual(my_tuple[-1], 'c')
        self.assertEqual(my_tuple[:-1], ('a', 'b'))


if __name__ == '__main__':
    unittest.main()
