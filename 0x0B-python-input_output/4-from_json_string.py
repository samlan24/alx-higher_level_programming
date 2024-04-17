#!/usr/bin/python3
"""This is a function that returns an python object"""
import json


def from_json_string(my_str):
    """returns a python data structure"""
    return json.loads(my_str)
