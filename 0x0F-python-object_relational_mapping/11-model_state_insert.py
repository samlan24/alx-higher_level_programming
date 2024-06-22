#!/usr/bin/python3

"""
Script that prints that
adds a state to the db
and prints its id
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":

    state_name = argv[4]
    # creating engine
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url)

    # a sessionmaker to manage sessions
    Session = sessionmaker(bind=engine)
    # this is a session object
    session = Session()
    Base.metadata.create_all(engine)

    # adding state
    state_to_add = State(name=state_name)
    session.add(state_to_add)

    # commit changes
    session.commit()

    # print the id of the new state
    print(f"{state_to_add.id}")

    # close the session
    session.close()
