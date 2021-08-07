"""
Testing insertions.
"""
import os

import backend.database.base as backend_base
from backend.database.insertions import add_occupation, create_entry
from backend.database.models import Occupation, Patient, Village
from backend.database.utils import get_latest_row, session_scope
from backend.tests.database import TEST_DB_PATH, TEST_ENGINE, TEST_SESSION


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
    with session_scope(TEST_SESSION) as session:
        village_count = len(session.query(Village).all())
        village_name = "this village should not exist"

        def create_repeat():
            village = create_entry(Village, 'village', village_name, session)
            session.add(village)
            session.commit()

        create_repeat()
        assert len(session.query(Village).all()) == village_count + 1

        create_repeat()  # No new row should have been created, so the count should stay the same as above.
        assert len(session.query(Village).all()) == village_count + 1


def test_add_occupation():
    """
    Test the add occupation function.
    """
    with session_scope(TEST_SESSION) as session:
        patient = Patient(
            first_name='J',
            last_name='D',
            date_of_birth='05-05-2005',
            gender='F',
        )

        occupation = add_occupation({
            'occupation_description': 'some description pertaining occupations',
            'occupation_title': 'CEO',
            'company': 'Evil Corp'
        }, patient=patient, existing_session=session)

        session.add(occupation)
        session.commit()

        occupation_result = get_latest_row(session, Occupation)
        patient_result = get_latest_row(session, Patient)

        assert patient_result.occupation[0] is occupation_result


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
