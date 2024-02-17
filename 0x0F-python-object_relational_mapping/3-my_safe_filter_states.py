#!/usr/bin/python3

'''
Displays all values in the states table of hbtn_0e_0_usa where name matches the argument (safe from SQL injection).
'''

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and state name from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Prepare SQL query with parameterized query
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute SQL query with the state name as parameter
    cursor.execute(sql_query, (state_name,))

    # Fetch and print the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()

