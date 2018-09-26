#!/usr/bin/env python3

import unittest
from user import User


class TestUser(unittest.TestCase):

    def test_add_attribute(self):

        user = User()

        # print(help(user))
        """
        Help on User in module python_collections_play.user object:
        class User(builtins.object)
         |  simplest possible class
         |  Python 3 class implicitly inherits from object
         |  Therefore implicitly inherits object constructor __init__(self)
         |  https://stackoverflow.com/questions/4015417/python-class-inherits-object
         |  
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
        """

        self.assertEqual(user.__dict__, {})

        # code outside a class can add an attribute to the class
        user.ball = 'red'
        self.assertEqual(user.ball, 'red')
        self.assertEqual(user.__dict__, {'ball': 'red'})


if __name__ == '__main__':
    unittest.main()
