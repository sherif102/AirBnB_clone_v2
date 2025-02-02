#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String, relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """amenity"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place",
                                   secondary=place_amenity,
                                   back_populates="amenities")
