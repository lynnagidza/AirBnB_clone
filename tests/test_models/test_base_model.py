#!/usr/bin/python3
"""
    Test module for base_model
"""
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """
        TestBaseModel Class
    """

    def setUp(self):
        """ Create an instance of the BaseModel class """
        self.base_model = BaseModel()

    def tearDown(self):
        """ Delete the instance of BaseModel class """
        del self.base_model

    def test_type(self):
        """ Test if the type of BaseModel class is a class """
        self.assertEqual(str(type(self.base_model)),
                         "<class 'models.base_model.BaseModel'>")

    def test_id(self):
        """ Test if BaseModel has unique ID """
        base_model2 = BaseModel()
        self.assertNotEqual(self.base_model.id, base_model2.id)

    def test_created_at(self):
        """ Test if BaseModel has 'created_at' attribute """
        self.assertTrue(hasattr(self.base_model, "created_at"))

    def test_updated_at(self):
        """ Test if BaseModel has 'updated_at' attribute """
        self.assertTrue(hasattr(self.base_model, "updated_at"))

    def test_str(self):
        """ Test the __str__ method of BaseModel """
        expected_output = f"[{type(self.base_model).__name__}] "\
            f"({self.base_model.id}) "\
            f"{self.base_model.__dict__}"

        self.assertEqual(expected_output, str(self.base_model))

    def test_save(self):
        """ Test the save method of BaseModel """
        self.base_model.save()
        self.assertNotEqual(self.base_model.created_at,
                            self.base_model.updated_at)

    def test_to_dict(self):
        """ Test the to_dict method of BaseModel """
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict["id"], self.base_model.id)
        self.assertEqual(base_model_dict["created_at"],
                         self.base_model.created_at.isoformat())
        self.assertEqual(base_model_dict["updated_at"],
                         self.base_model.updated_at.isoformat())
        self.assertEqual(base_model_dict["__class__"],
                         type(self.base_model).__name__)

    def test_new(self):
        """ Test the new method of FileStorage """
        storage = FileStorage()
        storage.reload()
        base_model = BaseModel()
        storage.new(base_model)
        key = f"{base_model.__class__.__name__}.{base_model.id}"
        self.assertIn(key, storage.all())

    def test_reload(self):
        """ Test the reload method of FileStorage """
        storage = FileStorage()
        base_model = BaseModel()
        key = f"{base_model.__class__.__name__}.{base_model.id}"
        storage.new(base_model)
        storage.save()
        os.remove("file.json")
        self.assertFalse(os.path.exists("file.json"))
        storage.reload()
        self.assertTrue(os.path.exists("file.json"))
        self.assertIn(key, storage.all())


if __name__ == '__main__':
    unittest.main()
