#!/usr/bin/env python3

"""
TODO:
it is possible to send data to a generator. Once you do that you have a 'coroutine'.
It's very simple to implement patterns like the mentioned Consumer/Producer with coroutines
because they have no need for Locks and therefore can't deadlock.
It's hard to describe coroutines without bashing threads,
so I'll just say coroutines are a very elegant alternative to threading

https://stackoverflow.com/questions/1756096/understanding-generators-in-python#1756156
"""


def mixed_generator(n):
    """
    mixed_generator yields 3 values, then if next is called again throws StopIteration exception
    https://stackoverflow.com/questions/1756096/understanding-generators-in-python#1756156
    :param n:
    :return: yielded value
    """
    # yield on first call to next
    yield n
    # yield on second call to next
    yield 'duck'
    # yield on third call to next
    yield n ** 4


def fib_generator():
    """
    generates an infinite stream
    call like
        list(itertools.islice(fib_generator(), 12))
    https://stackoverflow.com/questions/1756096/understanding-generators-in-python#1756156
    :return:
    """
    a, b = 0, 1
    while True:
        yield a
        # advance a and b, executes even though yield has yielded
        a, b = b, a + b

