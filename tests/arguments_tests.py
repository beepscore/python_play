#!/usr/bin/env python3

import unittest
from arguments import multiply_with_positional_args, add_with_kwargs


class TestArguments(unittest.TestCase):

    def test_multiply_with_positional_args(self):
        self.assertEqual(multiply_with_positional_args(*(3, 6)), 18)

    def test_add_with_kwargs(self):
        self.assertEqual(add_with_kwargs(**{'dog': 4, 'cat': 3}), 7)


if __name__ == '__main__':
    unittest.main()
