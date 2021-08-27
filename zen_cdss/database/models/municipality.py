"""
Municipality model.
"""

from sqlalchemy import Column, Integer, String

from zen_cdss.database.base import Base


class Municipality(Base):  # pylint: disable=too-few-public-methods
    """
    Municipality table.
    """
    __tablename__ = "municipality"

    id = Column(Integer, primary_key=True)
    municipality = Column(String(50))

    def __init__(self, municipality: str):
        self.municipality = municipality

    def __repr__(self):
        return f'Municipality(municipality="{self.municipality}")'
