#!/usr/bin/python3
"""
Defines 7-base_geometry
"""
class BaseGeometry:
    """ 7-base_geometry class """
    def area(self):
        """ area func """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer_validator func """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

