#!/usr/bin/python3
"""same_class
"""


def is_same_class(obj, a_class):
    """function that returns if the object is exactly an instance of the specified class or no
    Args:
        obj (_object): _description_
        a_class (class): _description_
    Returns:
        True: if object is an instance of class
        False: if it is not
    """

    return True if type(obj) is a_class else False
