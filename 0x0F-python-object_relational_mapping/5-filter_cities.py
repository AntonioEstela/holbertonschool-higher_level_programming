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

    cursor.execute("""SELECT cities.name FROM cities
                      INNER JOIN states ON cities.state_id = states.id
                      WHERE states.name = %(state_name)s
                      ORDER BY cities.id ASC;""", {'state_name': sys.argv[4]})

    states = cursor.fetchall()

    print(", ".join([row[0] for row in states]))

    cursor.close()
    database.close()
