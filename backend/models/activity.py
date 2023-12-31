#!/usr/bin/python3

"""
    This model create the activity data and inherits from
    the BaseModel.
"""

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Enum


class Activity(BaseModel, Base):
    """
        Representation of activity data.

        Args:
            BaseModel (_type_): class
            Base (_type_): sqlalchemy declarative_base
    """

    __tablename__ = "activities"
    school_id = Column(String(64), ForeignKey("schools.id"))
    pupil_id = Column(String(64), ForeignKey("pupils.id"))
    parent_id = Column(String(64), ForeignKey("parents.id"))

    action = Column(Enum('PICK-UP', 'DROP-OFF'), nullable=False)

    def __init__(self, *args, **kwargs):
        """initialize activity"""
        super().__init__(*args, **kwargs)
