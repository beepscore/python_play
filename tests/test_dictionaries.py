#!/usr/bin/env python3

import unittest
from collections import defaultdict


class TestDictionaries(unittest.TestCase):

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

    def test_enumerate(self):
        my_dict = {'a': 1, 'b': 5, 'd': -9}
        actual = []
        # to enumerate a dictionary use items()
        # python >= 3.6 dictionary maintains order
        for key, value in my_dict.items():
            actual.append(value)

        self.assertEqual(actual, [1, 5, -9])

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
        self.assertEqual(my_dict.get(3), 'foo')
        # get avoids KeyError if not in dictionary
        self.assertEqual(my_dict.get(8), None)

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
        self.assertEqual(nested['a'].get('b'), 3)

        # get avoids KeyError if not in dictionary
        self.assertEqual(nested['a'].get('c'), None)

    def test_dict_comprehension(self):
        my_dict = {key: key + 5 for key in range(0, 3)}
        self.assertEqual(my_dict, {0: 5, 1: 6, 2: 7})

    def test_defauldict_default_factory_int(self):

        """
        test collections.defaultdict
        supplies defaultdictionary default_factory a 'callable'. e.g. int, list
        default_factory = int tells defaultdict when adding a new key without a value, default value to int 0
        documentation examples mentions this is useful for counting
        https: // docs.python.org / 3.7 / library / collections.html  # collections.defaultdict
        """
        default_factory = int
        kwargs = {'a': 5, 'e': 9}
        my_defaultdict = defaultdict(default_factory, **kwargs)

        self.assertEqual(my_defaultdict, {'a': 5, 'e': 9})

        # defaultdict silently adds key c with default value 0
        self.assertEqual(my_defaultdict['c'], 0)
        # python >= 3.6 dictionary maintains key order
        self.assertEqual(my_defaultdict, {'a': 5, 'e': 9, 'c': 0})

        # get() doesn't trigger add key value pair
        self.assertEqual(my_defaultdict.get('d'), None)

        # can 'freeze' dict by setting defaultfactory = None
        # https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work#5900634

        my_defaultdict.default_factory = None

        # naive non-idiomatic unit test raising an exception
        # try:
        #     # now this will throw KeyError
        #     self.assertEqual(my_defaultdict['k'], 0)
        #     # execution path not get here
        #     self.assertTrue(False)
        # except KeyError as e:
        #     self.assertTrue(True)

        # pythonic unit test raising an exception uses a context manager
        # https://www.youtube.com/watch?v=6tNS--WetLI
        # https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/
        with self.assertRaises(KeyError):
            _ = my_defaultdict['k']


if __name__ == '__main__':
    unittest.main()
