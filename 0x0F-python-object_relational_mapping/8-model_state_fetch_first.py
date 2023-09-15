#!/usr/bin/python3
"""SQLAlchemy that connects a python script to a database"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    link = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(link)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f'{first_state.id}: {first_state.name}')
    else:
        print("Nothing")
