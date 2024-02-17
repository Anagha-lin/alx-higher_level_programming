#!/usr/bin/python3
"""Lists all State objects that contain the letter a from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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

    # Query State objects containing the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Display results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()

