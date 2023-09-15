#!/usr/bin/python3
"""Defining a Class called State"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# Defining the SQLAlchemy model class
Base = declarative_base()


class State(Base):
    """Class State that inherits from Base"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
