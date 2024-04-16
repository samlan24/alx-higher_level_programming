#!/usr/bin/python3
"""A module inheriting from list class"""


class MyList(list):
    """A class inheritance """

    def print_sorted(self):
        """prints list in ascending order"""
        print(sorted(self))
