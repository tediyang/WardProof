#!/usr/bin/python3

"""
    This model create the auxillary data and inherits from
    the BaseModel.
"""

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Enum, ForeignKey


class AuxillaryGuardian(BaseModel, Base):
    """
        Representation of auxillary_guardian data.

        Args:
            BaseModel (_type_): class
            Base (_type_): sqlalchemy declarative_base
    """

    __tablename__ = 'auxillaries'
    super_id = Column(String(64), ForeignKey('parents.id'))
    parent_id = Column(String(64), nullable=False)
    first_name = Column(String(64), nullable=False)
    last_name = Column(String(64), nullable=False)
    other_name = Column(String(64))
    gender = Column(Enum('MALE', 'FEMALE', 'OTHERS'))
    tag = Column(Enum('AUXILLARY-GUARDIAN'))

    def __init__(self):
        """initializes parent"""
        super().__init__()
