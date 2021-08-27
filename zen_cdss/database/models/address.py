"""
Address model.
"""

from typing import Optional

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from zen_cdss.database.base import Base
from zen_cdss.database.models.district import District
from zen_cdss.database.models.municipality import Municipality
from zen_cdss.database.models.patient import Patient
from zen_cdss.database.models.province import Province
from zen_cdss.database.models.village import Village


class Address(Base):  # pylint: disable=too-few-public-methods
    """
    Address table.
    """
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    address = Column(String)

    village_id = Column(Integer, ForeignKey('village.id'))
    village = relationship("Village", backref=backref("address"))

    municipality_id = Column(Integer, ForeignKey('municipality.id'))
    municipality = relationship("Municipality", backref=backref("address"))

    district_id = Column(Integer, ForeignKey('district.id'))
    district = relationship("District", backref=backref("address"))

    province_id = Column(Integer, ForeignKey('province.id'))
    province = relationship("Province", backref=backref("address"))

    patient_id = Column(Integer, ForeignKey('patient.id'))
    patient = relationship("Patient", backref="address")

    def __init__(
            self,
            address: str,
            village: Optional[Village],
            municipality: Optional[Municipality],
            district: Optional[District],
            province: Optional[Province],
            patient: Patient
    ):
        self.address = address
        self.village = village
        self.municipality = municipality
        self.district = district
        self.province = province
        self.patient = patient

    def __repr__(self):
        return f'Address(address="{self.address}", village={self.village}, municipality={self.municipality}, ' \
               f'district={self.district}, province={self.province}, patient={self.patient})'
