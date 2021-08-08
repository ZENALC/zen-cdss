"""
Testing insertions.
"""
import os
from datetime import datetime

import backend.database.base as backend_base
from backend.database.insertions import (add_address, add_contact_details, add_diagnosis, add_occupation, add_patient,
                                         create_entry)
from backend.database.models import Patient, Village
from backend.database.utils import session_scope
from backend.tests.database import TEST_DB_PATH, TEST_ENGINE, TEST_SESSION

TEST_PATIENT = Patient(  # Leverage this dummy patient for the tests below.
    first_name='J',
    last_name='D',
    date_of_birth='05-05-2005',
    gender='F',
)


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
        occupation = add_occupation({
            'occupation_description': 'some description pertaining occupations',
            'occupation_title': 'CEO',
            'company': 'Evil Corp'
        }, patient=TEST_PATIENT, existing_session=session)

        assert TEST_PATIENT.occupation[0] is occupation


def test_add_patient():
    """
    Test the add patient function.
    """
    with session_scope(TEST_SESSION) as session:
        patient = add_patient({
            'first_name': "Mike",
            'last_name': 'Smith',
            'gender': 'M',
            'date_of_birth': 'Aug 5 1995',
            'registration_date': '7 September, 2021',
            'referred_by': 'Sandy Smith',
            'accompanied_by': 'Thomas Jefferson',
            'family_diabetics': 'father, brother',
        }, existing_session=session)

        assert patient.first_name == 'Mike'
        assert patient.last_name == 'Smith'
        assert patient.gender == 'M'
        assert patient.date_of_birth == datetime(1995, 8, 5).date()
        assert patient.registration_date == datetime(2021, 9, 7).date()
        assert patient.referred_by == 'Sandy Smith'
        assert patient.accompanied_by == 'Thomas Jefferson'
        assert patient.family_diabetics == 'father, brother'


def test_add_contact_details():
    """
    Test the add contact details function.
    """
    with session_scope(TEST_SESSION) as session:
        contact_details = add_contact_details({
                'email': 'some@gmail.com',
                'phone': '781-202-2020',
            }, patient=TEST_PATIENT, existing_session=session)

        assert TEST_PATIENT.contact_details[0] is contact_details

        other_contact_details = add_contact_details({
                'email': 'lop@gmail.com',
                'phone': '784-120-1234',
            }, patient=TEST_PATIENT, existing_session=session)

        assert TEST_PATIENT.contact_details[1] is other_contact_details


def test_add_diagnosis():
    """
    Test the add diagnosis function.
    """
    with session_scope(TEST_SESSION) as session:
        diagnosis = add_diagnosis({
            'diagnosis': 'lung cancer',
            'diagnosis_advent': "Sep 5 2009"
        }, patient=TEST_PATIENT, existing_session=session)

        assert TEST_PATIENT.diagnosis[0] is diagnosis


def test_add_address():
    """
    Test the add address function.
    """
    with session_scope(TEST_SESSION) as session:
        address = add_address({
            'address': 'some address',
            'village': 'some village',
            'municipality': 'some municipality',
            'province': 'some province',
            'district': 'some district'
        }, patient=TEST_PATIENT, existing_session=session)

        assert TEST_PATIENT.address[0] is address
