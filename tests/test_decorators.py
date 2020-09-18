#!/usr/bin/env python3

import unittest
import sys
sys.path.append(".")
from python_play.decorators import Decorators


class TestDecorators(unittest.TestCase):

    def test_decorator(self):
        pretty = Decorators.make_pretty(Decorators.ordinary)
        pretty()

    def test_decorator_reassign(self):
        # often a decorated method is reassigned to it's own name
        ordinary = Decorators.make_pretty(Decorators.ordinary)
        ordinary()

    # def test_decorator2(self):
    #     Decorators.ordinary2()


if __name__ == '__main__':
    unittest.main()
