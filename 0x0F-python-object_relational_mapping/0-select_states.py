#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server using TCP/IP
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database,
                         unix_socket='/var/run/mysqld/mysqld.sock')

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to select all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()

