"""
Testing insertions.
"""
import os

import backend.database.base as backend_base
from backend.tests.database import TEST_DB_PATH, TEST_ENGINE


def setup_module():
    """
    Setup test module for testing.
    """
    backend_base.Base.metadata.create_all(TEST_ENGINE)


def teardown_module():
    """
    Teardown post testing.
    """
    os.remove(TEST_DB_PATH)


def test_create_entry():
    """
    Test the create entry function.
    """


def test_add_occupation():
    """
    Test the add occupation function.
    """


def test_add_patient():
    """
    Test the add patient function.
    """


def test_add_contact_details():
    """
    Test the add contact details function.
    """


def test_add_diagnosis():
    """
    Test the add diagnosis function.
    """


def test_add_address():
    """
    Test the add address function.
    """
