#!/usr/bin/python3

""" Some text """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """ Class Ciry that inherits from the class Base """

    __tablename__ = 'cities'

    id = Column(
        Integer, primary_key=True, autoincrement="auto", nullable=False,
        unique=True
    )

    name = Column(
        String(128), nullable=False
    )

    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False)
