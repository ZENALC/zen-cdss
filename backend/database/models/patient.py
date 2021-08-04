"""
Patient and other related models.
"""

from datetime import date
from typing import Optional, Union

from sqlalchemy import Column, Date, Integer, String

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

    def __repr__(self):
        return f'Patient(first_name={self.first_name}, last_name={self.last_name}, gender={self.gender}, ' \
               f'date_of_birth={self.date_of_birth}, registration_date={self.registration_date}, ' \
               f'referred_by={self.referred_by}, accompanied_by={self.accompanied_by}, ' \
               f'family_diabetics={self.family_diabetics})'

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
