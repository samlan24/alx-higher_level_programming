#!/usr/bin/python3
import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = '0987'
DB_NAME = 'hbtn_0e_0_usa'

# Connect to the database
db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASS, db=DB_NAME)

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

# Example 2: Describe the structure of the table
describe_query = f"DESCRIBE {table_name}"
cursor.execute(describe_query)

# Close the cursor and the connection
cursor.close()
db.close()
