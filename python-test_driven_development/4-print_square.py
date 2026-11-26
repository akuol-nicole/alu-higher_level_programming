#!/usr/bin/python3
"""Defines a square-printing function.

Provides `print_square` which validates an integer size parameter and
prints a square of `#` characters of that side length.
"""


def print_square(size):
    """Print a square with the `#` character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer (including floats and booleans).
        ValueError: If size is < 0.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
