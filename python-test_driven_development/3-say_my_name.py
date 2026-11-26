#!/usr/bin/python3
"""Defines a name-printing function.

Provides `say_my_name` which validates string inputs for first and last names
and prints a formatted greeting.
"""


def say_my_name(first_name, last_name=""):
    """Print 'My name is <first_name> <last_name>'.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print (defaults to empty string).
    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
