#!/usr/bin/python3

""" This is the model which all other will inherits from.

    Description:
    1. This model consists of three class attributes which are:
      - id: A unique primary key for each object generated.
      - created_at: datetime of object created.
      - updated_at: datetime when data is updated.

    2. It will provide three public instance attributes,
    where the unique id will be defined with uuid4, created at
    and updated at will be defined using datetime library.

    3. It will provide the following public instance methods:
      - __str__: return a string representation of the object attributes.
      - save: save any object generated to the storage.
      - to_dict: generate a dictionary format of the object attributes.
"""

from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
import uuid


time = "%Y-%m-%dT%H:%M:%S.%f"
Base = declarative_base()


class BaseModel:
    """ All other models will inherit from this BaseModel. """

    # Class attributes which other models will inherit.
    id = Column(String(64), primary_key=True)

    # Generate default values in the database.
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the public instances."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, time)
                    setattr(self, key, value)
                if key != "__class__":
                    setattr(self, key, value)
                if "id" not in self.__dict__:
                    self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """ string representation of the Object class """
        dic = self.__dict__.copy()
        dic.pop("_sa_instance_state", None)
        return f"[{self.__class__.__name__}] ({self.id}) {dic}"

    def save(self):
        """ updates the attribute 'updated_at' with the current datetime """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__

        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if "password" in new_dict:
            del new_dict["password"]

        return new_dict
