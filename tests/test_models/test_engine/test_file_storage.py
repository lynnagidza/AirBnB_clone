#!/usr/bin/python3
"""Unittest module for FileStorage class
"""
import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittest for FileStorage class
    """

    def setUp(self):
        """Setup for unittests
        """
        self.storage = FileStorage()
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()
        self.bm1.name = "Holberton"
        self.bm2.number = 89

    def tearDown(self):
        """Teardown for unittests
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test all method of FileStorage class
        """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test new method of FileStorage class
        """
        self.storage.new(self.bm1)
        all_objs = self.storage.all()
        obj_id = self.bm1.__class__.__name__ + "." + self.bm1.id
        self.assertIsNotNone(all_objs.get(obj_id))

    def test_save(self):
        """Test save method of FileStorage class
        """
        self.storage.new(self.bm2)
        self.storage.save()
        with open("file.json", mode="r", encoding="utf-8") as f:
            data = json.load(f)
        obj_id = self.bm2.__class__.__name__ + "." + self.bm2.id
        self.assertIsNotNone(data.get(obj_id))

    def test_reload(self):
        """Test reload method of FileStorage class
        """
        self.storage.new(self.bm1)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        obj_id = self.bm1.__class__.__name__ + "." + self.bm1.id
        self.assertIsNotNone(all_objs.get(obj_id))


if __name__ == "__main__":
    unittest.main()
