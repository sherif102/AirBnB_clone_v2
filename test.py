#!/usr/bin/python3
""" Test
"""
from models.base_model import BaseModel
from models.engine.db_storage import DBStorage
from models.state import State

st = State(name="Kwara")
print(st)



# kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
#                                                      '%Y-%m-%dT%H:%M:%S.%f')
# kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
#                                                      '%Y-%m-%dT%H:%M:%S.%f')