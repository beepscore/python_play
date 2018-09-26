#!/usr/bin/env python3


class InstanceVarClassVar:

    # reference this as InstanceVarClassVar.class_var
    class_var = 3

    def __init__(self, instance_var):

        self.instance_var = instance_var
