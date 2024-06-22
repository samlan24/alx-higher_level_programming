#!/usr/bin/python3

"""
prints all City objects
from the database hbtn_0e_14_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":

    # creating engine
    db_url = "mysql+pymysql://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url)

    # a sessionmaker to manage sessions
    Session = sessionmaker(bind=engine)
    # this is a session object
    session = Session()
    Base.metadata.create_all(engine)

    # printing city, id, and state
    results = session.query(City, State).join(State)

    for city, state in results.all():
        print(f"{state.name}: ({city.id}) {city.name}")

    session.commit()
    session.close()
