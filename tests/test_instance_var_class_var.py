#!/usr/bin/env python3

import unittest
from instance_var_class_var import InstanceVarClassVar


class TestInstanceVarClassVar(unittest.TestCase):
    """
    This class isn't meant to test Python's methods, but check my understanding.
    """

    def test_class_var(self):
        self.assertEqual(InstanceVarClassVar.class_var, 3)
        InstanceVarClassVar.class_var = 42
        self.assertEqual(InstanceVarClassVar.class_var, 42)

        instance0 = InstanceVarClassVar(0)
        self.assertFalse('class_var' in instance0.__dict__)
        self.assertTrue('instance_var' in instance0.__dict__)
        self.assertEqual(instance0.instance_var, 0)
        instance0.instance_var = 55
        self.assertEqual(instance0.instance_var, 55)

        self.assertFalse('some_new_var_not_declared_in_class' in instance0.__dict__)

        # assigning to a new attribute creates it
        # so assigning instance0.class_var = 356 would create a new attribute,
        # different from InstanceVarClassVar.class_var
        instance0.some_new_var_not_declared_in_class = 66
        self.assertTrue('some_new_var_not_declared_in_class' in instance0.__dict__)
        self.assertEqual(instance0.some_new_var_not_declared_in_class, 66)

        instance1 = InstanceVarClassVar(1)
        self.assertFalse('some_new_var_not_declared_in_class' in instance1.__dict__)
        self.assertEqual(instance1.instance_var, 1)

        instance1.instance_var = 77
        self.assertEqual(instance1.instance_var, 77)
        self.assertEqual(instance0.instance_var, 55)


if __name__ == '__main__':
    unittest.main()
