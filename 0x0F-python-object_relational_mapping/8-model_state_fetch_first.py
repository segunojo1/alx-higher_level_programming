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
    # Base.metadata.create_all(engine)
    session = Session(bind=engine)
    query = session.query(State).first()
    if query:
        print("{}: {}".format(query.id, query.name))
    else:
        print("Nothing")
