#!/usr/bin/python3
"""Creates a State with a City in the database hbtn_0e_100_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State and City objects
    california = State(name="California")
    san_francisco = City(name="San Francisco")

    # Add City to State and commit changes
    california.cities.append(san_francisco)
    session.add(california)
    session.commit()

    # Close session
    session.close()

