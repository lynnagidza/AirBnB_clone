#!/usr/bin/python3
"""
Unit tests for BaseModel class
"""

import unittest
import os
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class
    """

    def setUp(self):
        """Set up test environment"""
        self.model = BaseModel()

    def tearDown(self):
        """Tear down test environment"""
        del self.model
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_init_no_args(self):
        """Test instantiating BaseModel with no arguments"""
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_init_with_kwargs(self):
        """Test instantiating BaseModel with kwargs"""
        kwargs = {"id": "123", "created_at": "2022-04-19T17:14:25.709716",
                  "updated_at": "2022-04-19T17:14:25.709716",
                  "name": "test_model"}
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, "123")
        self.assertEqual(model.created_at,
                         datetime.datetime(2022, 4, 19, 17, 14, 25, 709716))
        self.assertEqual(model.updated_at,
                         datetime.datetime(2022, 4, 19, 17, 14, 25, 709716))
        self.assertFalse(hasattr(model, "name"))

    def test_init_with_empty_dict(self):
        """Test instantiating BaseModel with empty dictionary"""
        model = BaseModel({})
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))

    def test_str_method(self):
        """Test __str__ method"""
        string = (
            f"[{self.model.__class__.__name__}] "
            f"({self.model.id}) {self.model.__dict__}")

        self.assertEqual(str(self.model), string)

    def test_save_method(self):
        """Test save method"""
        self.model.save()
        self.assertNotEqual(self.model.created_at, self.model.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["created_at"],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         self.model.updated_at.isoformat())
        self.assertEqual(model_dict["__class__"],
                         self.model.__class__.__name__)


if __name__ == "__main__":
    unittest.main()
