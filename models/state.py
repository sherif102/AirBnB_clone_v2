#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String, relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state")

    @property
    def cities(self):
        """return the list of City instance linked"""
        from models import storage
        from models.city import City
        cities = []
        all = storage.all(City)
        for key, value in all.items():
            if self.id == value.state_id:
                cities.append(value)
        return cities
