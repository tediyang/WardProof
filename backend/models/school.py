#!/usr/bin/python3

"""
    This model create the school data and inherits from
    the BaseModel.

    Description:
    1. It provides the following class atrribute relationships:
      - activity: Fetch all the activities carried out with a
      particular child's id.
      - pupil: Fetch all the pupils enrolled in the school.

    2. Public instance method:
      - __setattr__: encrypt the school password using hashlib.md5.
"""

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from flask_bcrypt import generate_password_hash


class School(BaseModel, Base):
    """
        Representation of the School data

        Args:
            BaseModel (_type_): class
            Base (_type_): sqlalchemy declarative_base
    """

    __tablename__ = "schools"
    email = Column(String(64), nullable=False, unique=True)
    password = Column(String(64), nullable=False)
    name = Column(String(128), nullable=False)
    address = Column(String(64))
    city = Column(String(64))

    pupil = relationship("Pupil", backref="school")
    activity = relationship("Activity", backref="school", viewonly=True)

    def __init__(self, *args, **kwargs):
        """initialize school"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with encryption"""
        if name == "password":
            value = generate_password_hash(value).decode('utf8')
        super().__setattr__(name, value)
