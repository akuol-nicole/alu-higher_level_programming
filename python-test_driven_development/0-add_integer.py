#!/usr/bin/python3
"""Defines an integer addition function.

Provides `add_integer` which validates numeric inputs, casts floats to
integers, and returns their integer sum.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.
    Raises TypeError if either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
