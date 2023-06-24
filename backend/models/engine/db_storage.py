#!/usr/bin/python3
"""
    This is a DataBase Storage using MySQL

    Description:
    1. This DB consists of two private class attributes
      - __engine: connection with the mysql database.
      - __session: Each database session.
    2. The storage public instance methods include:
      - all: fetch all the data from a specific table.
      - new: add new object to the storage.
      - save: commit new changes to the storage.
      - delete: delete object from the storage.
      - update: update to data in the storage.
      - reload: setup the storage session.
      - close: remove the session.
"""

from models.basemodel import Base
from models.activity import Activity
from models.parent import Parent
from models.pupil import Pupil
from models.school import School
from models.auxillary import AuxillaryGuardian
from os import getenv
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

path = find_dotenv('wardproof.env')
load_dotenv(path)

classes = {"Activity": Activity, "Parent": Parent, "Pupil": Pupil,
           "School": School, 'AuxillaryGuardian': AuxillaryGuardian}


class DBStorage:
    """This is the DataBase Storage model that interacts with MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        user = getenv('WARDPROOF_USER')
        pwd = getenv('WARDPROOF_PWD')
        host = getenv('WARDPROOF_HOST')
        db = getenv('WARDPROOF_DB')

        self.__engine = create_engine('mysql+mysqlconnector://{}:{}@{}/{}'.
                                      format(user, pwd, host, db))

        if getenv('WARDPROOF_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls):
        """
            query on the current database session and return all
            data based on the provided cls.
        """
        # initialize the dict
        new_dict = {}
        # iterate of the items in classes and check for conditions
        for clss in classes:
            if cls == classes[clss] or cls == clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def update(self, cls, id, dic):
        """
            update the user's data.

            cls: class model
            id: unique id of Object (string)
            dic: data of key-value pairs to be updated
        """
        if cls not in classes.values():
            return None

        obj = self.get(cls, id)

        if obj:
            for key, val in dic.items():
                setattr(obj, key, val)
            obj.save()
            self.save()

    def get(self, cls, id):
        """A method to retrieve one object"""
        if cls and id:
            data = self.all(cls)
            search = "{}.{}".format(cls.__name__, id)
            if search in data.keys():
                return data[search]

        return None

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
