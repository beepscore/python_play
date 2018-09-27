#!/usr/bin/env python3

import unittest


class TestStr(unittest.TestCase):

    def test_type(self):
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
