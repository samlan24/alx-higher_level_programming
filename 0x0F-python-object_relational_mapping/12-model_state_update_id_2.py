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

    # creating engine
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url)

    # a sessionmaker to manage sessions
    Session = sessionmaker(bind=engine)
    # this is a session object
    session = Session()
    Base.metadata.create_all(engine)

    # change name of state
    update_state = session.query(State).filter_by(id=2).first()
    if update_state:
        update_state.name = "New Mexico"

    # commit changes
    session.commit()

    # close session
    session.close()
