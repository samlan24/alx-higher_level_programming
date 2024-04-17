#!/usr/bin/python3
"""This is a function that creates a object
from a json file"""
import json


def load_from_json_file(filename):
    """creating a json file"""
    with open(filename) as f:
        return json.loads(f)
