#!/usr/bin/python3

"""
    This model create the child data and inherits from
    the BaseModel.

    Description:
    1. It provides the following class atrribute relationships:
      - activity: Fetch all the activities carried out with a
      particular child's id.
      - auxillary_guardians: Fetch all the auxillary guardians attached
      to a particular child.
"""

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Enum, Date, ForeignKey
from sqlalchemy.orm import relationship


class Pupil(BaseModel, Base):
    """
        Representation of pupil data

        Args:
            BaseModel (_type_): class
            Base (_type_): sqlalchemy declarative_base
    """
    __tablename__ = "pupils"
    school_id = Column(String(64), ForeignKey('schools.id'))
    parent_id = Column(String(64), ForeignKey('parents.id'))  # Super-Guardian
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    other_name = Column(String(64))
    dob = Column(Date, nullable=False)
    allergy = Column(String(128))
    class_grade = Column(String(64), nullable=False)
    gender = Column(Enum('MALE', 'FEMALE', 'OTHERS'), nullable=False)
    parent_fullname = Column(String(64))  # Super-Guardian fullname

    activity = relationship("Activity", uselist=False, backref="pupil",
                            cascade="all, delete")

    def __init__(self):
        """ Initializes pupil """
        super().__init__()
