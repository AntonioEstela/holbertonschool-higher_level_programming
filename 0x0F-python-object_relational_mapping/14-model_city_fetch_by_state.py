#!/usr/bin/python3
""" Some text """

import sys
import sqlalchemy as db
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    """ Conecting to a database """
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                              .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                              pool_pre_ping=True)

    metadata = db.MetaData()

    Session = sessionmaker(bind=engine)
    session = Session()

    for c, s in session.query(City, State).filter(State.id == City.state_id):
        print('{}: ({}) {}'.format(s.name, c.id, c.name))

    session.commit()

    session.close()
