#!/usr/bin/python3
"""A function that checks instances"""


def is_same_class(obj, a_class):
    """checks whether object is instance of class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
