#!/usr/bin/env python3


def mixed_generator(n):
    """
    mixed_generator yields 3 values, then throws StopIteration exception
    https://stackoverflow.com/questions/1756096/understanding-generators-in-python#1756156
    :param n:
    :return:
    """
    yield n
    yield 'duck'
    yield n ** 4


