#!/usr/bin/python3
"""This is a function that returns dictionary description with
simple data structure """


def class_to_json(obj):
    """returns a dictionary representation"""
    return obj.__dict__
