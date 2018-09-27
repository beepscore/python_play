#!/usr/bin/env python3


class InstanceAttrClassAttr:
    """
    Python
    "What you really want to avoid is creating an attribute on the instance
    that has the same name as an attribute on the class"
    http://blog.lerner.co.il/python-attributes/
    """

    # add attribute to the class object, not to an instance of the class
    # This is roughly similar to a class variable.
    # In Swift, a variable declared here would be an instance variable unless annotated @static
    # reference this as InstanceVarClassVar.class_attr
    class_attr = 3

    def __init__(self, instance_attr):

        # add attribute to the instance
        # this is roughly similar to an instance variable
        self.instance_attr = instance_attr
