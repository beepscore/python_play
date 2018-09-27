#!/usr/bin/env python3

import unittest


class TestLists(unittest.TestCase):

    def test_type(self):
        """
        Python doesn't have a notion of "primitive" types
        everything is an object and has a type, including int and bool
        Some objects have a non 'builtin' type
        A variable doesn't have a type, but its value does.
        """
        # list
        my_list = [1, 5, -9]
        self.assertEqual(type(my_list), list)

    def test_slice(self):
        my_list = [9, 3, 5]
        self.assertEqual(my_list[-1], 5)
        self.assertEqual(my_list[:-1], [9, 3])

    def test_list_mixed_types(self):
        """
        list can contain different types. However this is atypical and could be confusing.
        """
        my_dict = {'a': 1, 'b': 5, 'd': -9}
        my_list = [1, 'k', my_dict]
        self.assertEqual(len(my_list), 3)
        self.assertEqual(my_list[0], 1)
        self.assertEqual(my_list[1], 'k')
        self.assertEqual(my_list[2], my_dict)


if __name__ == '__main__':
    unittest.main()
