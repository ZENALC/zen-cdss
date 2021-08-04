"""
File contain tests for database classes.
"""
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import backend.database.base as backend_base
from backend import TEST_DB_PATH
from backend.database.models import (Address, Company, ContactDetails, Diagnosis, District, Municipality, Occupation,
                                     OccupationTitle, Patient, Province, Village)

TEST_ENGINE = create_engine(f'sqlite:///{TEST_DB_PATH}')
TEST_SESSION = sessionmaker(bind=TEST_ENGINE)


def setup_module():
    """
    Setup test module for testing.
    """
    backend_base.Base.metadata.create_all(TEST_ENGINE)


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
    original_repr = repr(test_obj)

    generated_obj = eval(repr(test_obj))
    generated_repr = repr(generated_obj)

    assert original_repr == generated_repr, f"Expected: {original_repr}. Got: {generated_repr}"
