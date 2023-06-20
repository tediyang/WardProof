#!/usr/bin/python3

"""
    This model create the school data and inherits from
    the BaseModel.

    Description:
    1. It provides the following class atrribute relationships:
      - activity: Fetch all the activities carried out with a
      particular child's id.
      - auxillary_guardians: Fetch all the auxillary guardians attached
      to a particular child.
"""

from models.basemodel import BaseModel, Base

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class School(BaseModel, Base):
    """Representation of the School data"""
    __tablename__ = "schools"
    email = Column(String(64), nullable=False, unique=True)
    password = Column(String(64), nullable=False)
    name = Column(String(128), nullable=False)
    address = Column(String(64))
    city = Column(String(64))

    pupil = relationship("Pupil", backref="school")
    activity = relationship("Activity", backref="parent", viewonly=True)

    def __init__(self):
        """initialize school"""
        super().__init__()

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)