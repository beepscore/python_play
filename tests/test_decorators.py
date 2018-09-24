#!/usr/bin/env python3

import unittest
from python_collections_play.decorators import Decorators


class TestDecorators(unittest.TestCase):

    def test_decorator(self):
        pretty = Decorators.make_pretty(Decorators.ordinary)
        pretty()


if __name__ == '__main__':
    unittest.main()
