#!/usr/bin/python3
"""
lists all states with a name
starting with N.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states from the database.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute(
        "SELECT * FROM states "
        "WHERE name LIKE BINARY 'N%' "
        "ORDER BY id ASC"
    )

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
    db_cursor.close()
    db_connect.close()
