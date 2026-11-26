#!/usr/bin/python3
"""Defines unittests for models/base.py."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittests for Base class."""

    def test_auto_id(self):
        b1 = Base()
        self.assertIsNotNone(b1.id)

    def test_auto_id_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_passed_id(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_dict(self):
        res = Base.to_json_string([{'id': 12}])
        self.assertEqual(res, '[{"id": 12}]')

    def test_to_json_string_returns_str(self):
        res = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(res, str)

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_dict(self):
        res = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(res, [{'id': 89}])

    def test_from_json_string_returns_list(self):
        res = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(res, list)


if __name__ == "__main__":
    unittest.main()
