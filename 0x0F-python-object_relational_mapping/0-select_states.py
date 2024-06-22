#!/usr/bin/python3
import MySQLdb
from sys import argv

# Connect to the database
db = MySQLdb.connect(host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

# Create a cursor object to interact with the database
cursor = db.cursor()

# Example table name
table_name = 'states'

# Example 1: Select data from the table
select_query = f"SELECT * FROM {table_name}"
cursor.execute(select_query)

# Fetch all the rows from the executed query
rows = cursor.fetchall()

# Print the fetched rows (data)
for row in rows:
    print(row)

# Close the cursor and the connection
cursor.close()
db.close()
