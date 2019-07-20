#!/usr/bin/env python3

import unittest


class TestScope(unittest.TestCase):
    """
    test variable scope
    """

    def add_two(self, my_num):
        self.assertEqual(my_num, 3)
        my_num = 6
        self.assertEqual(my_num, 6)
        return my_num + 2

    def test_add_two(self):
        my_num = 3
        print("outer scope before call", my_num)
        self.assertEqual(my_num, 3)

        result = self.add_two(my_num)

        print("result", result)
        print("outer scope after call", my_num)
        self.assertEqual(my_num, 3)
