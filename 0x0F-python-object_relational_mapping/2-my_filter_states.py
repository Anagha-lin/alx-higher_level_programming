#!/usr/bin/python3

"""
Lists all states from the database hbtn_0e_0_usa where the name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Establish connection to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create a cursor object
    cur = db.cursor()

    # Execute SQL query to select states matching the provided state name
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))

    # Fetch and print the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()

