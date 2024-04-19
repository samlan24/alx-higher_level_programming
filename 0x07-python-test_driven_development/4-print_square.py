#!/usr/bin/python3
"""

This module has one function that prints a square with the character #

"""


def print_square(size):
    """prints square with character #

    Args:
        size: length of the square

    prints:
        square with character #

    Raises:
        TypeError: If size is not an integer and is a float and less than 0
        ValueError: if size is less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print('#' * size)
