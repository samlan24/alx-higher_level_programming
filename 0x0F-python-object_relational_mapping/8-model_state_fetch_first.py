#!/usr/bin/python3

"""
Script that lists the first state in the db
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

    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
    session.close()
