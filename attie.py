#!/usr/bin/env python3

import copy

class Attie:

    def __init__(self, a_dict, b_dict):

        # Caution after instantiation,
        # if caller changes a_dict this will change self.a_dict, which probably is undesired.
        # In Python dictionary is passed as a reference.
        # In Swift, dictionary is a value type, automatically acts as a copy, which is more thread safe.
        # https://developer.apple.com/swift/blog/?id=10
        self.a_dict = a_dict

        # make a deep copy. If caller changes b_dict this won't accidentally change self.b_dict
        # shallow copy vs deep copy
        # https://stackoverflow.com/questions/3975376/understanding-dict-copy-shallow-or-deep
        # https://stackoverflow.com/questions/2465921/how-to-copy-a-dictionary-and-only-edit-the-copy
        self.b_dict = copy.deepcopy(b_dict)
