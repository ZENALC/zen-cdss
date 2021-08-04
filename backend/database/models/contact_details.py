"""
Contact details model.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from backend.database.base import Base
from backend.database.models.patient import Patient


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

    def __repr__(self):
        return f'ContactDetails(phone_number="{self.phone_number}", email="{self.email}", patient={self.patient})'
