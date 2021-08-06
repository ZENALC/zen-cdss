"""
File contain tests for database classes.
"""
import datetime
import os
from typing import Type

import pytest
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import Session, sessionmaker

import backend.database.base as backend_base
from backend import TEST_DB_PATH
from backend.database.models import (Address, Company, ContactDetails, Diagnosis, District, Municipality, Occupation,
                                     OccupationTitle, Patient, Province, Village)
from backend.database.utils import session_scope

TEST_ENGINE = create_engine(f'sqlite:///{TEST_DB_PATH}')
TEST_SESSION = sessionmaker(bind=TEST_ENGINE)


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


def get_dummy_patient() -> Patient:
    """
    Returns a dummy patient object.
    :return: Dummy patient object.
    """
    return Patient(
        first_name='Joe',
        last_name='Regan',
        gender='M',
        date_of_birth='Sep 26, 1955',
        referred_by="someone",
        accompanied_by="no one",
        family_diabetics="no one"
    )


def get_latest_row(session: Session, object_class: Type) -> backend_base.Base:
    """
    Get the latest row by ID.
    :param session: Session object to use to get the latest row.
    :param object_class: Object class to get the latest row of.
    :return: Latest row of the object class provided.
    """
    return session.query(object_class).order_by(desc('id')).first()


@pytest.mark.parametrize(
    'test_obj',
    [
        Address(address="add", village=Village("vil"), municipality=Municipality('mun'), district=District('dis'),
                province=Province('prov'), patient=Patient("J", "D", "M", "1/1/1994")),

        Company(company='company'),

        ContactDetails(phone_number='781', email='l@gmail.com', patient=Patient("J", "D", "M", "1/1/1994")),

        Diagnosis(diagnosis="diagnosis", advent="August 19, 2009", patient=Patient("J", "D", "M", "1/1/1994")),

        District(district="district"),

        Municipality(municipality="municipality"),

        Occupation(patient=Patient("J", "D", "M", "1/1/1994"), description="desc", company=Company(company='company'),
                   occupation_title=OccupationTitle("occ")),

        OccupationTitle(occupation_title="software engineer"),

        Patient(first_name="J", last_name="D", gender="M", date_of_birth="1/1/1994"),

        Province(province="province"),

        Village(village="village")
    ]
)
def test_repr(test_obj):
    """
    Test the __repr__() function for the models. Mainly being tested to assert that they initialize correctly.
    :param test_obj: Test object.
    """
    # pylint: disable=eval-used
    original_repr = repr(test_obj)

    generated_obj = eval(repr(test_obj))
    generated_repr = repr(generated_obj)

    assert original_repr == generated_repr, f"Expected: {original_repr}. Got: {generated_repr}"


def test_patient():
    """
    Test logic for creating patients.
    """
    with session_scope(TEST_SESSION) as session:
        patient = get_dummy_patient()

        session.add(patient)
        session.commit()

        address = Address(
            address="hello address",
            village=Village("hello village"),
            province=Province("hello province"),
            municipality=Municipality("hello municipality"),
            district=District("hello district"),
            patient=patient
        )

        session.add(address)
        session.commit()

        result_patient: Patient = get_latest_row(session, Patient)

        assert result_patient.first_name == patient.first_name
        assert result_patient.last_name == patient.last_name
        assert result_patient.gender == patient.gender
        assert result_patient.date_of_birth == patient.date_of_birth
        assert result_patient.referred_by == patient.referred_by
        assert result_patient.accompanied_by == patient.accompanied_by
        assert result_patient.family_diabetics == patient.family_diabetics
        assert result_patient.address[0] is address


def test_address():
    """
    Testing logic for address models.
    """
    village = Village("some village")
    municipality = Municipality("some municipality")
    district = District("some district")
    province = Province("some province")
    patient = get_dummy_patient()

    address = Address(
        address="some address",
        village=village,
        municipality=municipality,
        district=district,
        province=province,
        patient=patient
    )

    with session_scope(TEST_SESSION) as session:
        session.add(address)
        session.commit()

        result_address: Address = get_latest_row(session, Address)

        assert result_address.address == "some address"
        assert result_address.village is village
        assert result_address.municipality is municipality
        assert result_address.district is district
        assert result_address.province is province
        assert result_address.patient is patient


def test_contact_details():
    """
    Testing logic for creating contact details.
    """
    phone_number = "781-000-000"
    email = "hello@gmail.com"
    patient = get_dummy_patient()

    contact_details = ContactDetails(
        phone_number=phone_number,
        email=email,
        patient=patient)

    with session_scope(TEST_SESSION) as session:
        session.add(contact_details)
        session.commit()

        result_contact_details: ContactDetails = get_latest_row(session, ContactDetails)

        assert result_contact_details.phone_number == phone_number
        assert result_contact_details.email == email
        assert result_contact_details.patient is patient


def test_diagnosis():
    """
    Test logic for creating diagnoses.
    """
    patient = get_dummy_patient()
    diagnosis = Diagnosis(
        diagnosis="some diagnosis",
        advent="Sep 5 2010",
        patient=patient
    )

    with session_scope(TEST_SESSION) as session:
        session.add(diagnosis)
        session.commit()

        result_diagnosis: Diagnosis = get_latest_row(session, Diagnosis)

        assert result_diagnosis.diagnosis == "some diagnosis"
        assert result_diagnosis.advent == datetime.date(2010, 9, 5)
        assert result_diagnosis.patient is patient


def test_occupation():
    """
    Test logic for creating occupations.
    """
    description = "some description"
    occupation_title = OccupationTitle("Software Engineer")
    company = Company("Zen Healthcare")
    patient = get_dummy_patient()
    occupation = Occupation(
        patient=patient,
        description=description,
        occupation_title=occupation_title,
        company=company
    )

    with session_scope(TEST_SESSION) as session:
        session.add(occupation)
        session.commit()

        result_occupation: Occupation = get_latest_row(session, Occupation)

        assert result_occupation.patient is patient
        assert result_occupation.description == description
        assert result_occupation.company is company
        assert result_occupation.occupation_title is occupation_title
