#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String, relationship
# from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")

    # if getenv('HBNB_TYPE_STORAGE') != 'db':
    #     def cities(self):
    #         """return the list of City"""
    #         cities = []
    #         objects = storage.all()
    #         for obj in objects.values():
    #             if getattr(obj, 'state_id') == self.id:
    #                 cities.append(obj)
    #         return cities
