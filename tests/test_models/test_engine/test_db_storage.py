#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models.__init__ import storage


class test_dbStorage(unittest.TestCase):
    """ Class to test the database storage """
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_db_connection(self):
        """test the db connection is an object"""
        connection = storage.con
        self.assertIsInstance(connection, object)

    def test_all_return(self):
        """test attributes in the DBStorage class"""
        columns = storage.all('states')
        self.assertIsInstance(columns, tuple)


if __name__ == "__main__":
    unittest.main()
