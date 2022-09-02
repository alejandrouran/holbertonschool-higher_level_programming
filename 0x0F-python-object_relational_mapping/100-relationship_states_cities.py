#!/usr/bin/python3
"""
prints the first State object from the database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    cf = State(name="California")
    cf.cities = [City(name="San Francisco")]
    session.add(cf)
    session.commit()
    session.close()
