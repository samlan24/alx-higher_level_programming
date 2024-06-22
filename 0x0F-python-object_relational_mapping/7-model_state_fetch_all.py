#!/usr/bin/python3

"""
Script that lists all State objects from the database
Using module SQLAlchemy
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":

    # creating engine
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url)

    # a sessionmaker to manage sessions
    Session = sessionmaker(bind=engine)
    # this is a session object
    session = Session()
    Base.metadata.create_all(engine)

    all_states = session.query(State).order_by(State.id).all()
    for a_state in all_states:
        print(f"{a_state.id}: {a_state.name}")
    session.close()
