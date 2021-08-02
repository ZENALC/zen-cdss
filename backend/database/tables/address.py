"""
Address related tables for patients.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from backend.database.base import Base


class Address(Base):
    """
    Address table.
    """
    __table__name = "address"

    id = Column(Integer, primary_key=True)
    tole_id = Column(Integer, ForeignKey('tole.id'))
    municipality_id = Column(Integer, ForeignKey('municipality.id'))
    district_id = Column(Integer, ForeignKey('district.id'))
    province_id = Column(Integer, ForeignKey('province.id'))

    def __init__(
            self,
            first_name: str,
            last_name: str
    ):
        self.first_name = first_name
        self.last_name = last_name


class Tole(Base):
    """
    Tole table.
    """
    __table__name = "tole"

    id = Column(Integer, primary_key=True)
    tole = Column(String(50))

    def __init__(
            self,
            tole: str
    ):
        self.tole = tole


class Municipality(Base):
    """
    Municipality table.
    """
    ___table__name = "municipality"

    id = Column(Integer, primary_key=True)
    municipality = Column(String(50))

    def __init__(
            self,
            municipality: str
    ):
        self.municipality = municipality


class District(Base):
    """
    District table.
    """
    __table__name = "district"

    id = Column(Integer, primary_key=True)
    district = Column(String(50))

    def __init__(
            self,
            district: str
    ):
        self.district = district


class Province(Base):
    """
    Province table.
    """
    __table__name = "province"

    id = Column(Integer, primary_key=True)
    province = Column(String(50))

    def __init__(
            self,
            province: str
    ):
        self.province = province
