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

# @property
    # def reviews(self):
    #     """return the list of review instance linked"""
    #     from models import storage
    #     from models.review import Review
    #     reviews = []
    #     all = storage.all(Review)
    #     for key, value in all.items():
    #         if self.id == value.place_id:
    #             reviews.append(value)
    #     return reviews


      # @property
    # def cities(self):
    #     """return the list of City instance linked"""
    #     from models import storage
    #     from models.city import City
    #     cities = []
    #     all = storage.all(City)
    #     for key, value in all.items():
    #         if self.id == value.state_id:
    #             cities.append(value)
    #     return cities