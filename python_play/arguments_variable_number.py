#!/usr/bin/env python3

"""
arguments *args and **kwargs
Can a variable number of arguments be passed to a function?
https://stackoverflow.com/questions/919680/can-a-variable-number-of-arguments-be-passed-to-a-function#919684
https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters
"""


def multiply_with_positional_args(*args):
    """
    :param args: a tuple with arbitrary number of positional arguments
    :return:
    """
    foo = args[0]
    bar = args[1]
    return foo * bar


def cat_plus_dog(**kwargs):
    """
    :param kwargs: a dictionary with arbitrary number of keyword arguments
    :return: sum of values of 'cat' and 'dog'
    """
    # get is safer method, if not in dictionary returns None instead of KeyError
    # https://stackoverflow.com/questions/11041405/why-dict-getkey-instead-of-dictkey#11041421
    a = kwargs.get('cat')
    b = kwargs.get('dog')

    if a is None:
        return b
    elif b is None:
        return a
    else:
        return a + b


def sum_of_kwargs_values(**kwargs):
    """
    :param kwargs: a dictionary with arbitrary number of keyword arguments
    :return: sum of values of all kwargs
    """
    return sum(kwargs.values())

