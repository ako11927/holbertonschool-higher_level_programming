#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    # Create a cursor object
    cursor = db.cursor()
    # Execute the query with BINARY for case-sensitive comparison
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'
ORDER BY id ASC")
    # Fetch all rows
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)
    # Close cursor and database connection
    cursor.close()
    db.close()
