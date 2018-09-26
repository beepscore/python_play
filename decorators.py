#!/usr/bin/env python3


class Decorators:
    """
    A decorator in Python is any callable Python object that is used to modify a function or a class.
    A reference to a function "func" or a class "C" is passed to a decorator and the decorator returns a modified function or class.
    The modified functions or classes usually contain calls to the original function "func" or class "C".
    https://www.python-course.eu/python3_decorators.php

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

    # threw TypeError 'staticmethod' object is not callable
    # https://stackoverflow.com/questions/45070196/python-decorator-for-class-method-and-static-method?noredirect=1&lq=1
    # @staticmethod
    # @make_pretty
    # def ordinary2():
    #     print('I am ordinary2')

##############

# outside of class Decorator
# example from https://www.python-course.eu/python3_decorators.php


def our_decorator(func):

    def function_wrapper(x):
        print('Before calling ' + func.__name__)
        func(x)
        print('After calling ' + func.__name__)

    return function_wrapper


@our_decorator
def foo(x):
    print('Hi, foo has been called with ' + str(x))


if __name__ == '__main__':

    foo('Hi')
    """
    Before calling foo
    Hi, foo has been called with Hi
    After calling foo
    """

