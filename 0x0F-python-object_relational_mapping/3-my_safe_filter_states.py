#!/usr/bin/python3
"""
returns name that matches the argument from
the states table
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    printing the argument
    """
    if len(argv) != 5:
        exit(1)

    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    db_state = argv[4]

    db_connect = MySQLdb.connect(
        host="localhost",
        user=db_user,
        port=3306,
        passwd=db_passwd,
        db=db_name
    )

    db_cursor = db_connect.cursor()

    query = (
        "SELECT * FROM states "
        "WHERE name LIKE BINARY %s "
        "ORDER BY id ASC"
    )

    db_cursor.execute(query, (db_state,))

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)

    db_cursor.close()
    db_connect.close()
