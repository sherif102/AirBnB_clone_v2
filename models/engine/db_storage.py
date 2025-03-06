#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import MySQLdb
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base


class DBStorage:
    """This class manages storage of hbnb models in
    MySQL database using sqlalchemy"""
    __engine = None
    __session = None
    models = [User, State, City, Amenity, Place, Review]

    def __init__(self):
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST", "localhost")
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
        HBNB_ENV = getenv("HBNB_ENV")

        self.__engine = create_engine(f"mysql+mysqldb://{HBNB_MYSQL_USER}:"
                                      f"{HBNB_MYSQL_PWD}@{HBNB_MYSQL_HOST}/"
                                      f"{HBNB_MYSQL_DB}", pool_pre_ping=True)
        self.__session = sessionmaker(bind=self.__engine)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

        self.reload()

    def all(self, cls=None):
        """query the database for the classname :> table supplied"""
        objects = {}
        if cls is not None:
            session = self.__session
            for x in session.query(cls).all():
                name = x.__class__.__name__
                objects[f'{name}.{x.id}'] = x
            return objects
        else:
            session = self.__session
            for mod in DBStorage.models:
                for x in session.query(mod).all():
                    name = x.__class__.__name__
                    objects[f'{name}.{x.id}'] = x
            return objects

    def new(self, obj):
        """creates new obj to the database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all transaction"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes the specify object from the database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_fact)

    def close(self):
        """call remove session"""
        self.__session.remove()
