#!/usr/bin/env python3

import unittest


class TestPythonCollections(unittest.TestCase):
    """
    This class isn't meant to test Python's methods, but check my understanding.
    """

    def test_types(self):
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

        # str
        my_str = 'hi mom'
        self.assertEqual(type(my_str), str)

        # list
        my_list = [1, 5, -9]
        self.assertEqual(type(my_list), list)

        # dictionary has type dict
        my_dict = {'a': 1, 'b': 5, 'd': -9}
        self.assertEqual(type(my_dict), dict)

    def test_tuple_slice(self):
        """
        slice works on tuple similar to list
        """
        my_tuple = ('a', 'b', 'c')
        self.assertEqual(my_tuple[-1], 'c')
        self.assertEqual(my_tuple[:-1], ('a', 'b'))

    def test_str_slice(self):
        """
        slice works on str similar to list
        """
        my_str = 'Slartibartfast'
        self.assertEqual(my_str[-1], 't')
        self.assertEqual(my_str[:-1], 'Slartibartfas')

    def test_dict_mixed_values(self):
        """
        dict values may have different types. This is not unusual.
        """
        my_list = [1, 'k']
        my_dict = {'a': 7, 'b': 'foo', 'd': my_list}
        self.assertEqual(len(my_dict.keys()), 3)
        self.assertEqual(my_dict['a'], 7)
        self.assertEqual(my_dict['b'], 'foo')
        self.assertEqual(my_dict['d'], my_list)

    def test_dict_mixed_keys(self):
        """
        dict keys may have different types.  I think this is atypical and could be confusing.
        keys must be hashable, presumably to construct a hash table
        https://docs.python.org/3/library/stdtypes.html#dict
        """
        my_dict = {'a': 7, 3: 'foo'}
        self.assertEqual(len(my_dict.keys()), 2)

        # https://stackoverflow.com/questions/40141901/cannot-do-type-is-tests-on-dict-keys-dict-values-dict-items
        # this fails because dict.keys() returns a "view object", not a list
        # self.assertEqual(my_dict.keys(), ('a', 3))

        self.assertEqual(type(my_dict.keys()), {}.keys().__class__)

        # python 3.7 guarantees dictionary maintains insertion order
        self.assertEqual(list(my_dict.keys()), ['a', 3])

        self.assertEqual(my_dict['a'], 7)
        self.assertEqual(my_dict[3], 'foo')

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
