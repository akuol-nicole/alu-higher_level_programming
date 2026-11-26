#!/usr/bin/python3
"""Defines unittests for models/square.py."""
import os
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Unittests for Square class."""

    def tearDown(self):
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_sq_one_arg(self):
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_sq_two_args(self):
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_sq_three_args(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_sq_four_args(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_sq_size_str(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_sq_x_str(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_sq_y_str(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_sq_size_neg(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_sq_x_neg(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_sq_y_neg(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_sq_size_zero(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s = Square(4, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 4")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 5)
        self.assertEqual(
            s.to_dictionary(),
            {'id': 5, 'size': 10, 'x': 2, 'y': 1}
        )

    def test_update_no_args(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual(str(s), "[Square] (10) 10/10 - 10")

    def test_update_1_arg(self):
        s = Square(10, 10, 10, 10)
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 10")

    def test_update_2_args(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 1)
        self.assertEqual(str(s), "[Square] (89) 10/10 - 1")

    def test_update_3_args(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 1, 2)
        self.assertEqual(str(s), "[Square] (89) 2/10 - 1")

    def test_update_4_args(self):
        s = Square(10, 10, 10, 10)
        s.update(89, 1, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_update_kwarg_id(self):
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89})
        self.assertEqual(str(s), "[Square] (89) 10/10 - 10")

    def test_update_kwarg_size(self):
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(str(s), "[Square] (89) 10/10 - 1")

    def test_update_kwarg_x(self):
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(str(s), "[Square] (89) 2/10 - 1")

    def test_update_kwarg_y(self):
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_create_id(self):
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_size(self):
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_create_x(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_create_y(self):
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one(self):
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            self.assertIn('"size": 1', f.read())

    def test_load_from_file_no_file(self):
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        s1 = Square(1, 0, 0, 7)
        Square.save_to_file([s1])
        res = Square.load_from_file()
        self.assertEqual(len(res), 1)
        self.assertEqual(str(res[0]), str(s1))


if __name__ == "__main__":
    unittest.main()
