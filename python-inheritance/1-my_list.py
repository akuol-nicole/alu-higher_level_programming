#!/usr/bin/python3
"""Defines a subclass of list called MyList."""


class MyList(list):
    """Represents a custom list that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order without modifying it."""
        print(sorted(self))
