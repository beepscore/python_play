#!/usr/bin/env python3

import unittest
from python_collections_play.attie import Attie


class TestPythonCollections(unittest.TestCase):
    """ test object attributes"""

    def test_mutate_attribute(self):

        sample_a_dict = {'a': 3}
        sample_b_dict = {'b': 14}
        attie = Attie(sample_a_dict, sample_b_dict)
        self.assertEqual(attie.a_dict, sample_a_dict)
        self.assertEqual(attie.b_dict, sample_b_dict)

        # mutate sample_a_dict
        sample_a_dict['c'] = 4
        self.assertEqual(sample_a_dict, {'a': 3, 'c': 4})
        # gack! this changed attie.a_dict too!
        self.assertEqual(attie.a_dict, {'a': 3, 'c': 4})

        # this assigns a new dictionary to sample_a_dict so doesn't affect attie.a_dict
        sample_a_dict = {'k': 5}
        self.assertEqual(attie.a_dict, {'a': 3, 'c': 4})

        # mutate sample_b_dict
        sample_b_dict['g'] = 17
        self.assertEqual(sample_b_dict, {'b': 14, 'g': 17})
        # didn't change attie.b_dict, because Attie.__init__ makes a deep copy
        self.assertEqual(attie.b_dict, {'b': 14})


if __name__ == '__main__':
    unittest.main()
