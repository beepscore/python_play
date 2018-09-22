#!/usr/bin/env python3

import unittest
from arguments import add_values


class TestArguments(unittest.TestCase):
    """
    This class isn't meant to test Python's methods, but check my understanding.
    """

    def test_add_values(self):
        self.assertEqual(add_values(**{'dog': 5, 'cat': 3}), 8)


if __name__ == '__main__':
    unittest.main()
