#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from app.db import Game, Review, User, GameUser

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///many_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace()