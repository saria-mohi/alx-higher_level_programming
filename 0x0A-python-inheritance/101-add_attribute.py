#!/usr/bin/python3
"""
Checks if an attribute can be added to an object.
"""


def add_attribute(an_obj, an_attr, a_value):
    """function that adds a new attribute to an object if it’s possible:
        Raise a TypeError exception, with the message can't add new attribute if the object can’t have new attribute
    Args:
        - an_obj: object to add the attribute to
        - an_attr: name of the attribute
        - a_value: value of the attribute to add
    """

    if not hasattr(an_obj, '__slots__') and not hasattr(an_obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(an_obj, '__slots__') and not hasattr(an_obj, an_attr):
        raise TypeError("can't add new attribute")

    setattr(an_obj, an_attr, a_value)
