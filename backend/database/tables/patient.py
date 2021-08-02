"""
Patient table.
"""

from sqlalchemy import Column, Date, Integer, String

from backend.database.base import Base


class Patient(Base):  # pylint: disable=too-few-public-methods
    """
    Patient table.
    """
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    date_of_birth = Column(Date)
    registration_date = Column(Date)

    def __init__(
            self,
            first_name: str,
            last_name: str,
            registration_date: str,
            date_of_birth: str
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.registration_date = registration_date
        self.date_of_birth = date_of_birth
