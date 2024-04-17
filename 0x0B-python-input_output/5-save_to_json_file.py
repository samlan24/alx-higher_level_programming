#!/usr/bin/python3
"""This is a function that writes an object to
a text file using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file
    using JSON"""
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dumps(my_obj, f)
