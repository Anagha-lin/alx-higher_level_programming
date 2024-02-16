#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine to connect to MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    # Create session maker bound to the engine
    Session = sessionmaker(bind=engine)

    # Create session object
    session = Session()

    # Query all State objects and sort them by id
    states = session.query(State).order_by(State.id).all()

    # Print State objects
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()

