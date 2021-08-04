"""
Init file.
"""

import os

BACKEND_PATH = os.path.dirname(__file__)
ROOT_PATH = os.path.dirname(BACKEND_PATH)

# TODO: Leverage PostgreSQL instead of SQLite.
DB_NAME = "zen_cdss.db"
DB_PATH = os.path.join(ROOT_PATH, DB_NAME)

TEST_DB_NAME = "zen_cdss_test.db"
TEST_DB_PATH = os.path.join(ROOT_PATH, TEST_DB_NAME)
