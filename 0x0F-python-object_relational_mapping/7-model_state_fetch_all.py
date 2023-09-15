#!/usr/bin/python3
"""SQLAlchemy that connects a python script to a database"""
from sqlalchemy import create_engine, Column, String, CHAR, Integer
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    link = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(link)

    Session = sessionmaker(bind=engine)
    session = Session()

    table_elements = session.query(State).all()

    for state in table_elements:
        print(f'{state.id}: {state.name}')
