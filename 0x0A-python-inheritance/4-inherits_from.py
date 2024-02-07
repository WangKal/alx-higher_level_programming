#!/usr/bin/python3
"""
Attribute 4-inherits_from
"""

def inherits_from(obj, a_class):
    """ 4-inherits_from func """
    if (type(obj) != a_class):
        return issubclass(type(obj), a_class)
    return False

