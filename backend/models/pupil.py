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
    """Representation of pupil data"""
    __tablename__ = "pupils"
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    other_name = Column(String(64))
    dob = Column(Date, nullable=False)
    class_grade = Column(String(64), nullable=False)
    gender = Column(Enum('MALE', 'FEMALE', 'OTHERS'), nullable=False)
    school_id = Column(String(64), ForeignKey('schools.id'), nullable=False)
    parent_id = Column(String(64), ForeignKey('parents.id')) #Super-Guardian
    parent_fullname = Column(String(64)) #Super-Guardian fullname

    activity = relationship("Activity", uselist=False, backref="pupil",
                            viewonly=True, cascade="all, delete")
    auxillary_guardians = relationship("AuxillaryGuardian",
                                       backref="pupil",
                                       cascade="delete",
                                       viewonly=True)

    def __init__(self):
        """ Initializes pupil """
        super().__init__()