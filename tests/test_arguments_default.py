#!/usr/bin/env python3

import unittest
from arguments_default import func_param_mutable_default_antipattern, func_param_immutable_default_safer


class TestArgumentsDefault(unittest.TestCase):

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
