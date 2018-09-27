#!/usr/bin/env python3

import unittest
from generators import mixed_generator


class TestGenerators(unittest.TestCase):

    def test_mixed_generator(self):

        expect_throw_stop_iteration_exception = False
        flag = False

        try:
            mixed = mixed_generator(2)
            # call mixed_generator three times to reach its last yield
            self.assertEqual(next(mixed), 2)
            self.assertEqual(next(mixed), 'duck')
            self.assertEqual(next(mixed), 16)

            expect_throw_stop_iteration_exception = True
            self.assertEqual(next(mixed), 'mixed will throw, except will catch and this comparison wont finish')

            # expect these statements wont be executed
            flag = True
            self.assertEqual(next(mixed), 'this assertion wont be executed')

        except StopIteration as e:
            print(e)
            self.assertTrue(expect_throw_stop_iteration_exception)
            self.assertFalse(flag)


if __name__ == '__main__':
    unittest.main()
