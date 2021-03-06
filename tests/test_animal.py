#!/usr/bin/env python3

import unittest
import sys
sys.path.append(".")
from python_play import animal


class TestAnimal(unittest.TestCase):

    def test_init(self):
        my_dog = animal.Dog('fido')
        self.assertEqual(my_dog.name, 'fido')
        self.assertEqual(my_dog.speak(), 'hi, woof')


if __name__ == '__main__':
    unittest.main()
