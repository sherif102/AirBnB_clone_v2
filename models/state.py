#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """return the list of City"""
            from models import storage
            city_list = []
            objects = storage.all()
            for obj in objects.values():
                if getattr(obj, 'state_id', None) == self.id:
                    city_list.append(obj)
            return city_list
