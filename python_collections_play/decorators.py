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

    # threw TypeError 'staticmethod' object is not callable
    # https://stackoverflow.com/questions/45070196/python-decorator-for-class-method-and-static-method?noredirect=1&lq=1
    # @staticmethod
    # @make_pretty
    # def ordinary2():
    #     print('I am ordinary2')
