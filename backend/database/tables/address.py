"""
Address related tables for patients.
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from backend.database.base import Base


class Address(Base):  # pylint: disable=too-few-public-methods
    """
    Address table.
    """
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    village_id = Column(Integer, ForeignKey('village.id'))
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
