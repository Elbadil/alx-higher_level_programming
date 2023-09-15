#!/usr/bin/python3
"""SQLAlchemy that connects a python script to a database"""
from sqlalchemy import create_engine, select
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == "__main__":
    link = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(link)

    Session = sessionmaker(bind=engine)
    session = Session()

    stmt = select(State.name, City.id, City.name).select_from(State).join(
                  City, State.id == City.state_id)

    cities_by_states = session.execute(stmt)

    for row in cities_by_states:
        print(f"{row[0]}: ({row[1]}) {row[2]}")

    session.close()
