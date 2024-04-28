#!/usr/bin/python3
""" all State objects from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy.orm import *
from sqlalchemy import *
from model_state import State, Base


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    newstate = State(name='Louisiana')
    session.add(newstate)
    new_instance = session.query(State).filter_by(name='Louisiana').first()
    print("{}".format(new_instance.id))
    session.flush()
    session.commit()
