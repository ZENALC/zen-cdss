"""
Database testing initialization.
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend import ROOT_PATH

TEST_DB_NAME = "zen_cdss_test.db"
TEST_DB_PATH = os.path.join(ROOT_PATH, TEST_DB_NAME)

TEST_ENGINE = create_engine(f'sqlite:///{TEST_DB_PATH}')
TEST_SESSION = sessionmaker(bind=TEST_ENGINE)
