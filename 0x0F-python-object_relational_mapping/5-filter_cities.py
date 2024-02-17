#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Construct the SQL query to retrieve cities of the given state
    query = "SELECT cities.name FROM cities \
             JOIN states ON cities.state_id = states.id \
             WHERE states.name=%s ORDER BY cities.id ASC"

    # Execute the query with state_name as parameter
    cursor.execute(query, (state_name,))

    # Fetch all the results
    results = cursor.fetchall()

    # Print the cities
    if results:
        print(", ".join(city[0] for city in results))

    # Close cursor and database connection
    cursor.close()
    db.close()

