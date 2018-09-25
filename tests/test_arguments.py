#!/usr/bin/env python3

import unittest
from python_collections_play.arguments import multiply_with_positional_args
from python_collections_play.arguments import cat_plus_dog, sum_of_kwargs_values
from python_collections_play.arguments import func_param_mutable_default_antipattern, func_param_immutable_default_safer


class TestArguments(unittest.TestCase):

    def test_multiply_with_positional_args(self):
        self.assertEqual(multiply_with_positional_args(*(3, 6)), 18)

    def test_cat_plus_dog(self):
        self.assertEqual(cat_plus_dog(**{}), None)
        self.assertEqual(cat_plus_dog(**{'dog': None}), None)
        self.assertEqual(cat_plus_dog(**{'dog': 4}), 4)
        self.assertEqual(cat_plus_dog(**{'dog': 4, 'cat': 3}), 7)
        # ignores zebra
        self.assertEqual(cat_plus_dog(**{'dog': 4, 'cat': 3, 'zebra': 9}), 7)

    def test_sum_of_kwargs_values(self):
        self.assertEqual(sum_of_kwargs_values(**{'dog': 4}), 4)
        self.assertEqual(sum_of_kwargs_values(**{'dog': 4, 'cat': 3}), 7)
        self.assertEqual(sum_of_kwargs_values(**{'dog': 4, 'cat': 3, 'zebra': 9}), 16)

    def test_func_param_with_mutable_default_antipattern(self):
        """
        calling func_param_with_mutable_default_antipattern reuses default collection
        """
        self.assertEqual(func_param_mutable_default_antipattern(), ['thing'])
        self.assertEqual(func_param_mutable_default_antipattern(), ['thing', 'thing'])
        self.assertEqual(func_param_mutable_default_antipattern(), ['thing', 'thing', 'thing'])

        self.assertEqual(func_param_mutable_default_antipattern(['wild']), ['wild', 'thing'])

    def test_func_param_immutable_default_safer(self):
        """
        calling func_param_immutable_default_safer doesn't reuse default collection
        """
        self.assertEqual(func_param_immutable_default_safer(), ['thing'])
        self.assertEqual(func_param_immutable_default_safer(), ['thing'])
        self.assertEqual(func_param_immutable_default_safer(), ['thing'])


if __name__ == '__main__':
    unittest.main()
