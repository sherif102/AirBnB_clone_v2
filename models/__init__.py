#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage as Storage
else:
    from models.engine.file_storage import FileStorage as Storage


storage = Storage()
storage.reload()
