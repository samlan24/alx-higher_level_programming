#!/usr/bin/python3
"""This is a function that appends a string
at the end of a text file"""


def append_write(filename="", text=""):
    """appends a string and returns the
    number of characters added"""
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
