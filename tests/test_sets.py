#!/usr/bin/env python3

import unittest


class TestSets(unittest.TestCase):

    def test_type(self):
        """
        Python doesn't have a notion of "primitive" types
        everything is an object and has a type, including int and bool
        Some objects have a non 'builtin' type
        A variable doesn't have a type, but its value does.
        """
        # set
        my_set = {1, 5, -9}
        self.assertEqual(type(my_set), set)

        my_frozenset = frozenset([1, 5, -9])
        self.assertEqual(type(my_frozenset), frozenset)

    def test_set_mixed_types(self):
        """
        set can contain different types. However this is atypical and could be confusing.
        """
        my_set = {1, 'a', False}
        self.assertEqual(len(my_set), 3)
        self.assertTrue('a' in my_set)

    def test_set_no_order(self):
        my_set = {1, 'a', False}
        expected_no_order = {'a', False, 1}
        self.assertEqual(my_set, expected_no_order)

    def test_set_union(self):
        set0 = {1, 'a', False}
        set1 = {'harvey', 'a'}
        # in a or b
        union = set0 | set1
        self.assertEqual(union, {1, 'a', False, 'harvey'})

    def test_set_intersection(self):
        set0 = {1, 'a', False}
        set1 = {'harvey', 'a'}
        # in a and b
        intersection = set0 & set1
        self.assertEqual(intersection, {'a'})

    def test_set_difference(self):
        set0 = {1, 'a', False}
        set1 = {'harvey', 'a'}
        # in a and not in b
        sym_diff = set0 - set1
        self.assertEqual(sym_diff, {1, False})

    def test_set_symmetric_difference(self):
        set0 = {1, 'a', False}
        set1 = {'harvey', 'a'}
        # in a or b but not both. == union - intersection
        sym_diff = set0 ^ set1
        self.assertEqual(sym_diff, {1, False, 'harvey'})
        union = set0 | set1
        intersection = set0 & set1
        self.assertEqual(sym_diff, union - intersection)

    def test_set_mutable(self):
        """
        set is mutable
        frozenset is immutable
        """
        my_set = {1, 'a', False}
        my_set.add('frog')
        self.assertEqual(my_set, {1, 'frog', False, 'a'})
        my_set.remove(False)
        self.assertEqual(my_set, {1, 'frog', 'a'})
        my_set.clear()
        self.assertEqual(my_set, set())


if __name__ == '__main__':
    unittest.main()
