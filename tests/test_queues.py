#!/usr/bin/env python3

import unittest
import queue


class TestQueues(unittest.TestCase):
    """
    can be used with threads.
    A different queue class can be used with processes
    https://docs.python.org/3.6/library/queue.html
    http://www.learn4master.com/programming-language/python/python-queue-for-multithreading
    """

    def test_queue(self):
        q = queue.Queue()
        q.put('a')
        q.put('b')
        q.put('c')
        # standard FIFO queue
        self.assertEqual(q.get(), 'a')
        self.assertEqual(q.get(), 'b')
        self.assertEqual(q.get(), 'c')

    def test_lifo_queue(self):
        q = queue.LifoQueue()
        q.put('a')
        q.put('b')
        q.put('c')
        self.assertEqual(q.get(), 'c')
        self.assertEqual(q.get(), 'b')
        self.assertEqual(q.get(), 'a')


if __name__ == '__main__':
    unittest.main()
