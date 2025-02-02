#!/usr/bin/python3
""" Test
"""
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.state import State

storage = DBStorage()

states = storage.all()
print(states)
print(list(states.values())[0])
print('***')
for x in states.values():
    print(x)