#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa: """

import MySQLdb
import sys

if __name__ == '__main__':

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    database = MySQLdb.connect('localhost', username, password, database_name)

    cursor = database.cursor()

    cursor.execute("""SELECT id, name FROM states WHERE name LIKE 'N%'
                      ORDER BY states.id;""")

    states = cursor.fetchall()

    for row in states:
        print(row)

    database.close()
