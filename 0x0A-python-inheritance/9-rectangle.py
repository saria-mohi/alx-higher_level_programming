#!/usr/bin/python3
"""
Creates a Rectangle class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)
    Private instance attributes:
        - width
        - height
    Public method area().
    Inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """Initializes an instance.
        Args:
            - width: width of the rectangle
            - heigth: height of the rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a formatted string."""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Computes the area of the Rectangle instance.
        Overwrites the area() method from BaseGeometry.
        """

        return self.__width * self.__height
