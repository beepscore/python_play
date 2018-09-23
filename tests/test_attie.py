#!/usr/bin/env python3

import unittest
from python_collections_play.attie import Attie


class TestPythonCollections(unittest.TestCase):

    def test_mutate_attribute(self):

        sample_dict = {'a': 3}
        attie = Attie(sample_dict)
        self.assertEqual(attie.my_dict, sample_dict)

        # mutate sample_dict
        sample_dict['b'] = 4
        self.assertEqual(sample_dict, {'a': 3, 'b': 4})
        # gack! this changed attie.my_dict too!
        self.assertEqual(attie.my_dict, {'a': 3, 'b': 4})


if __name__ == '__main__':
    unittest.main()
