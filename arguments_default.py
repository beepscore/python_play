#!/usr/bin/env python3

"""
generally avoid parameter with mutable default

# Default Parameter Values in Python
http://effbot.org/zone/default-values.htm

# “Least Astonishment” and the Mutable Default Argument
https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument?rq=1
"""


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

    "... especially important to understand when a default parameter is a mutable object,
    such as a list or a dictionary: if the function modifies the object
    (e.g. by appending an item to a list), the default value is in effect modified.
    This is generally not what was intended.
    A way around this is to use None as the default,
    and explicitly test for it in the body of the function
    https://docs.python.org/3/reference/compound_stmts.html#function-definitions

    :return: collection by appending 'thing'
    """
    if collection is None:
        # safer pattern, instantiate a new mutable object inside the function, not as a parameter default.
        collection = []

    collection.append("thing")
    return collection
