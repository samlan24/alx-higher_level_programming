#!/usr/bin/python3
"""A function that checks if an object
is an instance of a specified class
"""


def inherits_from(obj, a_class):
    """checks whether object is instance of class"""
    if issubclass(obj, a_class):
        return True
    else:
        return False
