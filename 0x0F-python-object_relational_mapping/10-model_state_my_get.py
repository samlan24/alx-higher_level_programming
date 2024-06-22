#!/usr/bin/python3

"""
Script that prints the id of state
entered as an argument
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":

    # getting the state name
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

    # prints states id
    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print(f"{state.id}")
    else:
        print("Not found")
    session.close()
