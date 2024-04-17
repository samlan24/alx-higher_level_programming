#!/usr/bin/python3
import json
"""This is a function that returns JSON representation
of an object"""


def to_json_string(my_obj):
    """returns JSON representation"""
    return json.dumps(my_obj)
