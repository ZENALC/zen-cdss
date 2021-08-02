"""
Patient and other related tables.
"""
from datetime import date
from typing import Optional, Union

from dateutil import parser
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.database.base import Base


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

    def __init__(
            self,
            first_name: str,
            last_name: str,
            gender: str,
            date_of_birth: Union[str, date],
            registration_date: Optional[Union[str, date]] = None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = self.parse_gender(gender)
        self.date_of_birth = self.parse_date(date_of_birth)
        self.registration_date = self.parse_date(registration_date, null_ok=True)

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

    @staticmethod
    def parse_date(date_object: Union[str, date], null_ok: bool = False) -> date:
        """
        Helper function to parse dates and return as date objects.
        :param null_ok: Boolean whether null date objects are valid or not.
        :param date_object: Date object to parse.
        :return: Parsed date object.
        """
        if isinstance(date_object, date):
            return date_object

        if date_object is None and null_ok:
            return date.today()

        return parser.parse(date_object).date()


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


class OccupationTitle(Base):  # pylint: disable=too-few-public-methods
    """
    Occupation title.
    """
    __tablename__ = "occupation_title"

    id = Column(Integer, primary_key=True)
    occupation_title = Column(String)


class Company(Base):  # pylint: disable=too-few-public-methods
    """
    Company table.
    """
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    company = Column(String)
