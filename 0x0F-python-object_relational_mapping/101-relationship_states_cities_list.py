#!/usr/bin/python3
""" all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy.orm import *
from sqlalchemy import *
from relationship_city import City
from relationship_state import State, Base


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).order_by(State.id)
    # Access the data from the result
    for state in results:
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f'    {city.id}: {city.name}')
