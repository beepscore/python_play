#!/usr/bin/env python3

import unittest
import itertools
from generators import fib_generator, generator0, mixed_generator


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

    def test_mixed_generator_loop(self):

        mixed = mixed_generator(2)
        results = []

        # loop implicitly calls next,
        # and if all values have been yielded loop exits without throwing StopIteration exception
        for value in mixed:
            results.append(value)

        self.assertEqual(results, [2, 'duck', 16])

    def test_fib_generator(self):
        actual = list(itertools.islice(fib_generator(), 12))
        self.assertEqual(actual, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

    def test_generator0(self):
        g0 = generator0()
        self.assertEqual(next(g0), 4)
        self.assertEqual(next(g0), 9)
        self.assertEqual(next(g0), 16)


if __name__ == '__main__':
    unittest.main()
