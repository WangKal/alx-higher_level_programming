#!/usr/bin/python3
"""
Defines basegeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectanle details """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area func """
        return self.__width * self.__height

    def __str__(self):
        """ __str__ func"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

