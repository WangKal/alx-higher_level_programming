#!/usr/bin/python3
"""
Define myInt
"""
class MyInt(int):
    """ class myint details """
    def __eq__(self, other):
        """eq func """
        return self - other != 0

    def __ne__(self, other):
        """ ne func """
        return self - other == 0
