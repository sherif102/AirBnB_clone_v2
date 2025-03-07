#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String, Integer, Float
from models.base_model import ForeignKey, relationship
from sqlalchemy import Table

metadata = Base.metadata
place_amenity = Table("place_amenity", metadata,
                      Column('place_id', String(60),
                             ForeignKey("places.id"), nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey("amenities.id"), nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer(), nullable=False, default=0)
    number_bathrooms = Column(Integer(), nullable=False, default=0)
    max_guest = Column(Integer(), nullable=False, default=0)
    price_by_night = Column(Integer(), nullable=False, default=0)
    latitude = Column(Float())
    longitude = Column(Float())
    # amenity_ids = []
    user = relationship("User", back_populates="places")
    # cities = relationship("City", back_populates="places")
    reviews = relationship("Review", back_populates="place")
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False, back_populates="place_amenities")
