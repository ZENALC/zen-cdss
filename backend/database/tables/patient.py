"""
Patient table.
"""

from sqlalchemy import Column, Integer, String, Date
from backend.database.base import Base


class Patient(Base):
    """
    Patient database table.
    """
    __table__name = "patients"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    date_of_birth = Column(Date)

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
