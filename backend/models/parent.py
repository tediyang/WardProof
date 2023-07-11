#!/usr/bin/python3

"""
    This model create the parent data and inherits from
    the BaseModel.

    Description:
    1. It provides the following public instaance method:
      - __setattr__: encrypt the parent password using hashlib.md5
"""

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Enum, Date
from sqlalchemy.orm import relationship
from flask_bcrypt import generate_password_hash


class Parent(BaseModel, Base):
    """
        Representation of parent data.

        Args:
            BaseModel (_type_): class
            Base (_type_): sqlalchemy declarative_base
    """

    __tablename__ = 'parents'
    email = Column(String(64), nullable=False, unique=True)
    password = Column(String(64), nullable=False)
    first_name = Column(String(64))
    last_name = Column(String(64))
    other_name = Column(String(64))
    gender = Column(Enum('MALE', 'FEMALE', 'OTHERS'))
    tag = Column(Enum('SUPER-GUARDIAN', 'AUXILLARY-GUARDIAN'))
    dob = Column(Date)
    activity = relationship("Activity", backref="parent", viewonly=True)
    children = relationship("Pupil", backref="parent", cascade="delete")
    auxillary_guardians = relationship("AuxillaryGuardian",
                                       backref="parent",
                                       cascade="delete")

    def __init__(self, *args, **kwargs):
        """initialize parent"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with encryption"""
        if name == "password":
            value = generate_password_hash(value).decode('utf8')
        super().__setattr__(name, value)
