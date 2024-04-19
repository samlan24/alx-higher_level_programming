#!/usr/bin/python3
"""

This module has one function that prints first and last names

"""


def say_my_name(first_name, last_name=""):
    """prints first and last names

    Args:
        first_name: first argument
        last_name: second argument

    prints:
        first_name and last_name

    Raises:
        TypeError: If either of the arguments not stringsan integer or a float
    """
    
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
