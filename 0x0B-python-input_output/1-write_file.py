#!/usr/bin/python3
"""This is a function that returns the
number of characters written"""


def write_file(filename="", text=""):
    """returns number of characters
    written"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
