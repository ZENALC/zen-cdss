"""
Company model.
"""

from sqlalchemy import Column, Integer, String

from backend.database.base import Base


class Company(Base):  # pylint: disable=too-few-public-methods
    """
    Company table.
    """
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    company = Column(String)

    def __init__(self, company: str):
        self.company = company

    def __repr__(self):
        return f'Company(company="{self.company}")'
