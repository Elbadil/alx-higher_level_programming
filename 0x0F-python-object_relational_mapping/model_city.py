#!/usr/bin/python3
"""SQLAlchemy that connects a python script to a database"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from model_state import Base, State
from sys import argv


class City(Base):
    """Defining a class City that inherits From Base"""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)


if __name__ == "__main__":
    link = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(link)
    Base.metadata.create_all(engine)
