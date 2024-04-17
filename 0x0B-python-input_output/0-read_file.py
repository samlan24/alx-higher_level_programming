#!/usr/bin/python3
"""This is a function that reads a text file"""


def read_file(filename=""):
    """file reading function"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
