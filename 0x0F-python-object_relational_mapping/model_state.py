#!/usr/bin/python3
"""
contains the class definition
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State Class"""
    __tablename__ = 'states'
    id = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    name = Colums(String(128), nullable=False)
