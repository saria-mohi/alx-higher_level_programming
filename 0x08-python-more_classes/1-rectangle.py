#!/usr/bin/python3
"""Rectangle1"""


class Rectangle:
    """ Rectangle1 class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("Enter width as an integer")
        if value < 0:
            raise ValueError("width >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("Enter height as an integer")
        if value < 0:
            raise ValueError("height >= 0")
        self.__height = value

