"""
File that will create the DB engine and session.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from backend import DB_PATH

engine = create_engine(f'sqlite:///{DB_PATH}')
Session = sessionmaker(bind=engine)

Base = declarative_base()
