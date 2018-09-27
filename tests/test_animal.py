#!/usr/bin/env python3

import unittest
import animal


class TestAnimal(unittest.TestCase):

    def test_init(self):
        my_dog = animal.Dog('fido')
        self.assertEqual(my_dog.name, 'fido')


if __name__ == '__main__':
    unittest.main()
