"""
District model.
"""

from sqlalchemy import Column, Integer, String

from backend.database.base import Base


class District(Base):  # pylint: disable=too-few-public-methods
    """
    District table.
    """
    __tablename__ = "district"

    id = Column(Integer, primary_key=True)
    district = Column(String(50))

    def __init__(self, district: str):
        self.district = district

    def __repr__(self):
        return f'District(district="{self.district}")'
