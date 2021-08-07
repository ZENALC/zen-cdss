"""
Database testing initialization.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend import TEST_DB_PATH

TEST_ENGINE = create_engine(f'sqlite:///{TEST_DB_PATH}')
TEST_SESSION = sessionmaker(bind=TEST_ENGINE)
