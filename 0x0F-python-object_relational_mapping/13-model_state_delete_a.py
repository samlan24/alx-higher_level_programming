#!/usr/bin/python3

"""
Script that prints that
deletes states with letter a
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

    # deleting states
    deleted_states = session.query(State).filter(State.name.contains('a'))
    if deleted_states:
        for state in deleted_states:
            session.delete(state)

        # commiting changes
        session.commit()

        # closing session
        session.close()
