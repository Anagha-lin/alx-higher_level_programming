#!/usr/bin/python3

'''
Prints all rows from the states table of a specified database
that match a given state name.
'''

import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) >= 5:
        # Establish a connection to the MySQL database
        db_connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
        
        # Create a cursor object
        cursor = db_connection.cursor()
        
        # Get the state name from command-line argument
        state_name = sys.argv[4]
        
        # Execute the SQL query to retrieve matching rows
        cursor.execute(
            'SELECT * FROM states WHERE CAST(name AS BINARY) LIKE ' +
            'CAST("{}" AS BINARY) ORDER BY id ASC;'.format(state_name)
        )
        
        # Fetch and print the results
        results = cursor.fetchall()
        for result in results:
            print(result)
        
        # Close the database connection
        db_connection.close()

