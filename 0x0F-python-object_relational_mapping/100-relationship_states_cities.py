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
    newstate = State(name='California')
    newcity = City(name="San Francisco")
    newstate.cities.append(newcity)
    session.add(newstate)
    # new_instance = session.query(State).filter_by(name='Louisiana').first()
    # print("{}".format(new_instance.id))
    session.flush()
    session.commit()
