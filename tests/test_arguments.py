#!/usr/bin/env python3

import unittest
from python_collections_play.arguments import multiply_with_positional_args, cat_plus_dog


class TestArguments(unittest.TestCase):

    def test_multiply_with_positional_args(self):
        self.assertEqual(multiply_with_positional_args(*(3, 6)), 18)

    def test_cat_plus_dog(self):
        self.assertEqual(cat_plus_dog(**{'dog': 4, 'cat': 3}), 7)
        self.assertEqual(cat_plus_dog(**{'dog': 4, 'cat': 3, 'zebra': 9}), 7)


if __name__ == '__main__':
    unittest.main()
