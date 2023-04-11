#!/usr/bin/python3
"""Module 0-lookup
function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """Returns the list of the attributes and methods of obj
    """
    return dir(obj)
