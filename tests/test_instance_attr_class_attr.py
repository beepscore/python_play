#!/usr/bin/env python3

import unittest
import sys
sys.path.append(".")
from python_play.instance_attr_class_attr import InstanceAttrClassAttr


class TestInstanceAttrClassAttr(unittest.TestCase):

    def test_class_attr(self):

        # print(InstanceVarClassVar.__dict__)
        """
        {'__module__': 'instance_var_class_var', 'class_attr': 3,
        '__init__': <function InstanceVarClassVar.__init__ at 0x10cce00d0>,
        '__dict__': <attribute '__dict__' of 'InstanceVarClassVar' objects>,
        '__weakref__': <attribute '__weakref__' of 'InstanceVarClassVar' objects>, '__doc__': None}
        """

        self.assertEqual(InstanceAttrClassAttr.class_attr, 3)
        InstanceAttrClassAttr.class_attr = 42
        self.assertEqual(InstanceAttrClassAttr.class_attr, 42)

        instance0 = InstanceAttrClassAttr(0)
        # print(dir(instance0))
        """
        ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
        '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
        '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
        '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
        'class_attr', 'instance_attr']
        """

        # print(instance0.__dict__)
        # {'instance_attr': 0}

        self.assertFalse('class_attr' in instance0.__dict__)
        self.assertTrue('instance_attr' in instance0.__dict__)
        self.assertEqual(instance0.instance_attr, 0)
        instance0.instance_attr = 55
        self.assertEqual(instance0.instance_attr, 55)

        self.assertFalse('some_new_attr_not_defined_in_class' in instance0.__dict__)

        # assigning to a new attribute creates it
        # so assigning instance0.class_attr = 356 would add a new attribute,
        # different from InstanceVarClassVar.class_attr
        instance0.some_new_attr_not_defined_in_class = 66
        # print(instance0.__dict__)
        # {'instance_attr': 55, 'some_new_attr_not_defined_in_class': 66}

        self.assertTrue('some_new_attr_not_defined_in_class' in instance0.__dict__)
        self.assertEqual(instance0.some_new_attr_not_defined_in_class, 66)

        instance1 = InstanceAttrClassAttr(1)
        self.assertFalse('some_new_attr_not_defined_in_class' in instance1.__dict__)
        self.assertEqual(instance1.instance_attr, 1)

        instance1.instance_attr = 77
        self.assertEqual(instance1.instance_attr, 77)
        self.assertEqual(instance0.instance_attr, 55)


if __name__ == '__main__':
    unittest.main()
