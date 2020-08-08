#!/usr/bin/python3

""" Some text """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Class state that inherits from the class Base """

    __tablename__ = 'states'

    id = Column(
        Integer, primary_key=True, autoincrement="auto", nullable=False,
        unique=True
    )

    name = Column(
        String(128), nullable=False
    )
