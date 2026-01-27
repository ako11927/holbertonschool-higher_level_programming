#!/usr/bin/python3
"""
Lists all cities of a state from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    
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
    
    # Execute the query with parameterized input for safety
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))
    
    # Fetch all rows
    rows = cursor.fetchall()
    
    # Extract city names and join them with comma and space
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))
    
    # Close cursor and database connection
    cursor.close()
    db.close()
