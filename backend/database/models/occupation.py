"""
Occupation model.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.database.base import Base
from backend.database.models.company import Company
from backend.database.models.occupation_title import OccupationTitle
from backend.database.models.patient import Patient


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

    def __init__(self, patient: Patient, description: str, occupation_title: OccupationTitle, company: Company):
        self.patient = patient
        self.description = description
        self.occupation_title = occupation_title
        self.company = company

    def __repr__(self):
        return f'Occupation(patient={self.patient}, description="{self.description}", ' \
               f'occupation_title={self.occupation_title}, company={self.company})'
