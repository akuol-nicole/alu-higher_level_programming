#!/usr/bin/python3
"""Defines unittests for models/rectangle.py."""
import io
import os
import sys
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittests for Rectangle class."""

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

    def test_rect_two_args(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rect_three_args(self):
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rect_four_args(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_rect_five_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_rect_width_str(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rect_height_str(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rect_x_str(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rect_y_str(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rect_width_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rect_height_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rect_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rect_height_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rect_x_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rect_y_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_xy(self):
        r = Rectangle(2, 2)
        cap = io.StringIO()
        sys.stdout = cap
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(cap.getvalue(), "##\n##\n")

    def test_display_no_y(self):
        r = Rectangle(2, 2, 2)
        cap = io.StringIO()
        sys.stdout = cap
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(cap.getvalue(), "  ##\n  ##\n")

    def test_display_xy(self):
        r = Rectangle(2, 2, 2, 1)
        cap = io.StringIO()
        sys.stdout = cap
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(cap.getvalue(), "\n  ##\n  ##\n")

    def test_to_dictionary(self):
        r = Rectangle(10, 2, 1, 9, 5)
        self.assertEqual(
            r.to_dictionary(),
            {'id': 5, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        )

    def test_update_no_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (10) 10/10 - 10/10")

    def test_update_1_arg(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_2_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 1/10")

    def test_update_3_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 1/2")

    def test_update_4_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 3/10 - 1/2")

    def test_update_5_args(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_update_kwarg_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89})
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")

    def test_update_kwarg_width(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 1/10")

    def test_update_kwarg_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 1/2")

    def test_update_kwarg_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(str(r), "[Rectangle] (89) 3/10 - 1/2")

    def test_update_kwarg_y(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")

    def test_create_id(self):
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_width(self):
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_create_height(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_create_x(self):
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_create_y(self):
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        )
        self.assertEqual(r.y, 4)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_one(self):
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            self.assertIn('"width": 1', f.read())

    def test_load_from_file_no_file(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_exists(self):
        r1 = Rectangle(1, 2, 0, 0, 7)
        Rectangle.save_to_file([r1])
        res = Rectangle.load_from_file()
        self.assertEqual(len(res), 1)
        self.assertEqual(str(res[0]), str(r1))


if __name__ == "__main__":
    unittest.main()
