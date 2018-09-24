#!/usr/bin/env python3

import unittest
from python_collections_play.user import User


class TestUser(unittest.TestCase):

    def test_add_attribute(self):

        user = User()
        print(help(user))
        self.assertEqual(user.__dict__, {})

        # code outside a class can add an attribute to the class
        user.ball = 'red'
        self.assertEqual(user.ball, 'red')
        self.assertEqual(user.__dict__, {'ball': 'red'})

