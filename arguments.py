#!/usr/bin/env python3


def multiply_with_positional_args(*args):
    """
    https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters
    :param args: a tuple with arbitrary number of positional arguments
    :return:
    """
    foo = args[0]
    bar = args[1]
    return foo * bar


def cat_plus_dog(**kwargs):
    """
    https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters
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
    https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters
    :param kwargs: a dictionary with arbitrary number of keyword arguments
    :return: sum of values of all kwargs
    """
    return sum(kwargs.values())


def func_param_mutable_default_antipattern(collection=[]):
    """
    Do not put a mutable object as the default value of a function parameter,
    because the same object is reused on multiple calls.
    https://codehabitude.com/2013/12/24/python-objects-mutable-vs-immutable/
    :param collection: a mutable collection with an undesirable mutable default
    :return: collection by appending 'thing'
    """
    collection.append('thing')
    return collection


def func_param_immutable_default_safer(collection=None):
    """
    :param collection: a collection. default None which is immutable and therefor safer.
    In general avoid defaulting a parameter to a mutable object,
    because the same object is reused on multiple calls.
    https://codehabitude.com/2013/12/24/python-objects-mutable-vs-immutable/
    :return: collection by appending 'thing'
    """
    if collection is None:
        # safer pattern, instantiate a new mutable object inside the function, not as a parameter default.
        collection = []

    collection.append("thing")
    return collection
