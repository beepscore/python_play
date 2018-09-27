#!/usr/bin/env python3


class Animal:

    def __init__(self, name: str):
        self.name = name


class Dog(Animal):
    """
    Dog inherits from Animal
    """

    def __init__(self, name: str):
        """
        Note that the syntax changed in Python 3.0:
        you can just say super().__init__()
        instead of super(ChildB, self).__init__()
        https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods#576183
        :param name:
        """
        super().__init__(name)


