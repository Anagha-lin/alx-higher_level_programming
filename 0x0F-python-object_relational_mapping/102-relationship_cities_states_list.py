#!/usr/bin/python3
"""Lists all City objects with their corresponding State objects"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Database connection
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all cities with their corresponding states
    cities = session.query(City).order_by(City.id).all()

    # Print cities and corresponding states
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close session
    session.close()

