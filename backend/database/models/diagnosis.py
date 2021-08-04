"""
Diagnosis model.
"""

from datetime import date
from typing import Union

from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.database.base import Base
from backend.database.models.patient import Patient
from backend.database.utils import parse_date


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

    def __repr__(self):
        return f'Diagnosis(diagnosis={self.diagnosis}, advent={self.advent}, patient={self.patient})'
