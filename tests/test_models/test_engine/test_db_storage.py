#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.__init__ import storage
from models import *


class test_dbStorage(unittest.TestCase):
    """ Class to test the database storage """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_save(self):
        """test the db connection is an object"""
        storage.new(State(name="Ekiti"))
        storage.save()
        db_len = len(storage.all(State))

        storage.new(State(name="Osun"))
        storage.save()

        self.assertEqual(db_len, len(storage.all(State)) - 1)

    def test_all_return(self):
        """test attributes in the DBStorage class"""
        columns = storage.all(State)
        self.assertIsInstance(columns, dict)


if __name__ == "__main__":
    unittest.main()
