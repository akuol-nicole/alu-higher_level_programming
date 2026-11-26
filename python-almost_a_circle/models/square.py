#!/usr/bin/python3
"""Defines a square class.

Provides `Square` inheriting from `Rectangle` with a `size` property getter
and setter, positional/keyword attribute updates, and string representation.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """Assign positional or keyword arguments to attributes.

        Args:
            *args: Positional arguments in order: id, size, x, y.
            **kwargs: Key/value pairs of attributes to update (skipped if
                args is non-empty).
        """
        if args and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for attr, val in zip(attrs, args):
                if attr == "id" and val is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    setattr(self, attr, val)
        elif kwargs:
            for k, v in kwargs.items():
                if k == "id" and v is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    setattr(self, k, v)
