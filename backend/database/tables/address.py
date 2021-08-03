"""
Address related tables for patients.
"""
from typing import Optional

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from backend.database.base import Base
from backend.database.tables.patient import Patient


class Village(Base):  # pylint: disable=too-few-public-methods
    """
    Village table.
    """
    __tablename__ = "village"

    id = Column(Integer, primary_key=True)
    village = Column(String(50))

    def __init__(
            self,
            village: str
    ):
        self.village = village


class Municipality(Base):  # pylint: disable=too-few-public-methods
    """
    Municipality table.
    """
    __tablename__ = "municipality"

    id = Column(Integer, primary_key=True)
    municipality = Column(String(50))

    def __init__(
            self,
            municipality: str
    ):
        self.municipality = municipality


class District(Base):  # pylint: disable=too-few-public-methods
    """
    District table.
    """
    __tablename__ = "district"

    id = Column(Integer, primary_key=True)
    district = Column(String(50))

    def __init__(
            self,
            district: str
    ):
        self.district = district


class Province(Base):  # pylint: disable=too-few-public-methods
    """
    Province table.
    """
    __tablename__ = "province"

    id = Column(Integer, primary_key=True)
    province = Column(String(50))

    def __init__(
            self,
            province: str
    ):
        self.province = province


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
