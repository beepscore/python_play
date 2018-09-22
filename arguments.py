#!/usr/bin/env python3


def multiply_with_positional_args(*args):
    """
    https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters
    :param args: a tuple with positional arguments
    :return:
    """
    foo = args[0]
    bar = args[1]
    return foo * bar


def add_with_kwargs(**kwargs):
    """
    https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters
    :param kwargs: a dictionary with keyword arguments
    :return:
    """
    # get is safer method, if not in dictionary returns None instead of KeyError
    # https://stackoverflow.com/questions/11041405/why-dict-getkey-instead-of-dictkey#11041421
    a = kwargs.get('cat')
    b = kwargs.get('dog')
    return a + b
