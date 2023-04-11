#!/usr/bin/python3
"""
Creates a class that inherits from int.
"""


class MyInt(int):
    """
    MyInt is a rebel. MyInt has == and != operators inverted
    """

    def __eq__(self, other):
        """Equality becomes inequality."""

        return super().__ne__(other)

    def __ne__(self, other):
        """Inequality becomes equality."""

        return super().__eq__(other)
