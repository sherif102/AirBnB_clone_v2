#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base, String
from models.base_model import Column, ForeignKey, relationship
from models.state import State


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    # state = relationship("State", back_populates="cities")
    places = relationship("Place", backref="cities")
