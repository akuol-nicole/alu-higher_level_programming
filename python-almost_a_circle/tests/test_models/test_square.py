#!/usr/bin/python3
"""Defines unittests for models/square.py."""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(10), Rectangle)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_size_getter_setter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)
        self.assertEqual(8, s.width)
        self.assertEqual(8, s.height)


class TestSquareValidation(unittest.TestCase):
    """Unittests for testing validation of Square attributes."""

    def test_invalid_size_type(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)

    def test_invalid_x_type(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)

    def test_invalid_y_type(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, "invalid")

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)


class TestSquareMethods(unittest.TestCase):
    """Unittests for testing area, display, __str__, update, to_dictionary."""

    @staticmethod
    def capture_stdout(sq, method):
        """Captures and returns text printed to stdout."""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_area(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_str_method(self):
        s = Square(4, 2, 1, 12)
        self.assertEqual("[Square] (12) 2/1 - 4", str(s))

    def test_display_size_x_y(self):
        s = Square(3, 2, 2, 0)
        capture = TestSquareMethods.capture_stdout(s, "display")
        self.assertEqual("\n\n  ###\n  ###\n  ###\n", capture.getvalue())

    def test_update_args(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 2, 3, 4)
        self.assertEqual("[Square] (89) 3/4 - 2", str(s))

    def test_update_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(id=89, x=1, size=2, y=3)
        self.assertEqual("[Square] (89) 1/3 - 2", str(s))

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())


if __name__ == "__main__":
    unittest.main()
