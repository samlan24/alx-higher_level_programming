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

    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]

    # creating engine
    db_url = f'mysql+pymysql://{db_user}:{db_passwd}@localhost:3306/{db_name}'
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
