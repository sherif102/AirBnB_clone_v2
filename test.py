#!/usr/bin/python3
from models.base_model import BaseModel
from models.place import Place
from models import storage
# model = BaseModel()
# print(model)
# dic = {'name': 'California', 'population': '2421'}
# print(model.__dict__.update(dic))
# print(model)
storage.new(Place())
storage.new(BaseModel())
print([x.id for x in list(storage.all().values())])