#!/usr/bin/python3
""" Module - test_console.py
    Author: Sheriff Abiodun """

from models import storage
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class test_HBNBConsole(unittest.TestCase):
    """tests the console"""
    def test_create_output(self):
        """tests that the object is created and id is returned"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            ids = [x.id for x in list(storage.all().values())]
            self.assertIn(output.getvalue().strip(), ids)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd
                             ('create State name="California"'))
            ids = [x.id for x in list(storage.all().values())]
            self.assertIn(output.getvalue().strip(), ids)
            obj = storage.all()[f'State.{output.getvalue().strip()}']
            self.assertEqual("California", obj.name)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(output.getvalue().strip(),
                             '** class name missing **')


if __name__ == "__main__":
    unittest.main()
