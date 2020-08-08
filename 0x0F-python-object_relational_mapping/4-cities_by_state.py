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

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities " +
                 "JOIN states ON cities.state_id = states.id ORDER BY id ASC;")
    rows = curs.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    database.close()
