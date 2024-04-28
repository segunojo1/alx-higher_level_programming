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
    value = sys.argv[4]
    session = Session(bind=engine)
    query = session.query(State)\
        .filter(State.name.__eq__(value)).first()
    if query is None:
        print('Not found')
    else:
        print("{}".format(query.id))
