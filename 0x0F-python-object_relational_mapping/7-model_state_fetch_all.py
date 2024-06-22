#!/usr/bin/python3

"""
python file that contains the
class definition of a State and an
instance Base = declarative_base()
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":

    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]

    db_url = f'mysql+pymysql://{db_user}:{db_passwd}@localhost/{db_name}'
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    all_states = session.query(State).order_by(State.id).all()
    for a_state in all_states:
        print(f"{a_state.id}: {a_state.name}")
