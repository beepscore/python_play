#!/usr/bin/env python3

import unittest


class TestDictionaries(unittest.TestCase):
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
        # dictionary has type dict
        my_dict = {'a': 1, 'b': 5, 'd': -9}
        self.assertEqual(type(my_dict), dict)

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

    def test_dict_keys_mixed_types(self):
        """
        dict keys may have different types.  I think this is atypical and could be confusing.
        keys must be hashable, in order to construct a hash table
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

    def test_dict_key_tuple(self):
        """
        tuple containing only hashables can be used as a key because it is hashable
        """
        my_tuple = ('a', 'b')
        my_dict = {my_tuple: 7}
        self.assertEqual(my_dict[my_tuple], 7)

        my_hash = hash(my_tuple)
        # e.g. 7438149540147407425
        self.assertIsNotNone(my_hash)
        self.assertEqual(type(my_hash), int)

    def test_nested_dict(self):
        nested = dict()
        # didn't work
        # nested['a']['b'] = 3
        nested['a'] = {'b': 3}
        # print(nested)
        self.assertEqual(nested['a']['b'], 3)

    # TODO: consider add default dict


if __name__ == '__main__':
    unittest.main()
