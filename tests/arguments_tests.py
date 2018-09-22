#!/usr/bin/env python3

import unittest
from arguments import multiply_with_positional_args, add_values


class TestArguments(unittest.TestCase):
    """
    This class isn't meant to test Python's methods, but check my understanding.
    """

    def test_multiply_with_positional_args(self):
        self.assertEqual(multiply_with_positional_args(*(15, 11)), 26)

    def test_add_values(self):
        self.assertEqual(add_values(**{'dog': 5, 'cat': 3}), 8)


if __name__ == '__main__':
    unittest.main()
