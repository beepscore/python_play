#!/usr/bin/env python3

import unittest
import decimal


class TestType(unittest.TestCase):
    """
    This class isn't meant to test Python's methods, but check my understanding.
    """

    def test_type(self):
        """
        Python doesn't have a notion of "primitive" types
        everything is an object and has a type, including int and bool
        Some objects have a non 'builtin' type
        A variable doesn't have a type, but its value does.
        """
        # bool
        self.assertEqual(type(False), bool)

        # integer has type int
        self.assertEqual(type(3), int)

        # float
        self.assertEqual(type(3.14), float)

        # decimal- must import it
        y = decimal.Decimal(5)
        self.assertEqual(type(y), decimal.Decimal)

        # str
        my_str = 'hi mom'
        self.assertEqual(type(my_str), str)

    def test_str_slice(self):
        """
        slice works on str similar to list
        """
        my_str = 'Slartibartfast'
        self.assertEqual(my_str[-1], 't')
        self.assertEqual(my_str[:-1], 'Slartibartfas')


if __name__ == '__main__':
    unittest.main()
