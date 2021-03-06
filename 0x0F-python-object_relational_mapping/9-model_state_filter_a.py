#!/usr/bin/python3
""" Some text """

import sys
import sqlalchemy as db
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    """ Conecting to a database """
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                              .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                              pool_pre_ping=True)

    metadata = db.MetaData()

    Session = sessionmaker(bind=engine)
    session = Session()

    for data in session.query(State).filter(State.name.like('%a%')):
        print('{}: {}'.format(data.id, data.name))

    session.close()
