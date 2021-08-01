"""
File that will create the DB engine and session.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite://')
Session = sessionmaker(bind=engine)

Base = declarative_base()
