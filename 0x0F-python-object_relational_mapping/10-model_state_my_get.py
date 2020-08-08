#!/usr/bin/python3
""" Some text """

import sys
import sqlalchemy as db
from model_state import Base, State
from sqlalchemy import text

if __name__ == '__main__':

    """ Conecting to a database """
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                              .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                              pool_pre_ping=True)

    metadata = db.MetaData()

    conn = engine.connect()
    ins = text("INSERT INTO states (name) VALUES ('Louisiana')")
    result = conn.execute(ins)

    print_id = text("SELECT id, name FROM states WHERE name = 'Louisiana';")
    result = conn.execute(print_id).fetchall()

    try:
        if result[0] is not None:
            for i in result:
                print('{}'.format(i[0]))
    except IndexError:
        pass

    session.close()
