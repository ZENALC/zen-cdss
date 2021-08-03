"""
Patient and other related tables.
"""
from datetime import date
from typing import Optional, Union

from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.database.base import Base
from backend.database.utils import parse_date


class Patient(Base):  # pylint: disable=too-few-public-methods
    """
    Patient table.
    """
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True)

    first_name = Column(String(50))
    last_name = Column(String(50))
    gender = Column(String(1))
    date_of_birth = Column(Date)
    registration_date = Column(Date)
    referred_by = Column(String)
    accompanied_by = Column(String)
    family_diabetics = Column(String)

    def __init__(
            self,
            first_name: str,
            last_name: str,
            gender: str,
            date_of_birth: Union[str, date],
            registration_date: Optional[Union[str, date]] = None,
            referred_by: str = None,
            accompanied_by: str = None,
            family_diabetics: str = None
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = self.parse_gender(gender)
        self.date_of_birth = parse_date(date_of_birth)
        self.registration_date = parse_date(registration_date, null_ok=True)
        self.referred_by = referred_by
        self.accompanied_by = accompanied_by
        self.family_diabetics = family_diabetics

    @staticmethod
    def parse_gender(gender: str) -> str:
        """
        Parse gender and return parsed gender value.
        :param gender: Gender to parse.
        :return: Parsed gender value.
        """
        gender_upper = gender.upper()
        if gender_upper in {'MALE', 'M'}:
            return 'M'

        if gender_upper in {'FEMALE', 'F'}:
            return 'F'

        raise ValueError(f'Expected gender to be "M" or "F". Got: {gender}')


class Diagnosis(Base):  # pylint: disable=too-few-public-methods
    """
    Diagnosis table.
    """
    __tablename__ = "diagnosis"

    id = Column(Integer, primary_key=True)
    diagnosis = Column(String)
    advent = Column(Date)

    patient_id = Column(Integer, ForeignKey("patient.id"))
    patient = relationship("Patient", backref="diagnosis")

    def __init__(self, diagnosis: str, patient: Patient, advent: Union[str, date] = None):
        self.diagnosis = diagnosis
        self.advent = parse_date(advent)
        self.patient = patient


class ContactDetails(Base):  # pylint: disable=too-few-public-methods
    """
    Contact details table.
    """
    __tablename__ = "contact_details"

    id = Column(Integer, primary_key=True)

    phone_number = Column(String)
    email = Column(String)

    patient_id = Column(Integer, ForeignKey("patient.id"))
    patient = relationship("Patient", backref="contact_details")

    def __init__(
            self,
            phone_number: str,
            email: str,
            patient: Patient
    ):
        self.phone_number = phone_number
        self.email = email
        self.patient = patient


class Occupation(Base):  # pylint: disable=too-few-public-methods
    """
    Occupation table.
    """
    __tablename__ = "occupation"

    id = Column(Integer, primary_key=True)
    description = Column(String)

    occupation_title_id = Column(Integer, ForeignKey("occupation_title.id"))
    occupation_title = relationship("OccupationTitle", backref="occupation")

    company_id = Column(Integer, ForeignKey("company.id"))
    company = relationship("Company", backref="occupation")

    def __init__(self, patient: Patient, description: str, occupation_title: str, company: str):
        self.patient = patient
        self.description = description
        self.occupation_title = occupation_title
        self.company = company


class OccupationTitle(Base):  # pylint: disable=too-few-public-methods
    """
    Occupation title.
    """
    __tablename__ = "occupation_title"

    id = Column(Integer, primary_key=True)
    occupation_title = Column(String)

    def __init__(self, occupation_title: str):
        self.occupation_title = occupation_title


class Company(Base):  # pylint: disable=too-few-public-methods
    """
    Company table.
    """
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    company = Column(String)

    def __init__(self, company: str):
        self.company = company
