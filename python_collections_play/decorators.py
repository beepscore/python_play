#!/usr/bin/env python3


class Decorators:
    """
    a decorator is a callable that returns a callable
    https://www.programiz.com/python-programming/decorator
    """

    @staticmethod
    def make_pretty(func):
        def my_decorator():
            print('I got decorated')
            # call the passed in function
            func()

        # return my_decorator
        return my_decorator

    @staticmethod
    def ordinary():
        print('I am ordinary')

