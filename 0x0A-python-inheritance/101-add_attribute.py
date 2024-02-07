#!/usr/bin/python3
"""
attribute dd_attribute
"""

def add_attribute(obj, a, v):
    """ add_attribute func """
    res = getattr(obj, "__doc__", None)
    if res is None:
        setattr(obj, a, v)
    else:
        raise TypeError("can't add new attribute")

