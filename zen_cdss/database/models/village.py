"""
Village model.
"""

from sqlalchemy import Column, Integer, String

from zen_cdss.database.base import Base


class Village(Base):  # pylint: disable=too-few-public-methods
    """
    Village table.
    """
    __tablename__ = "village"

    id = Column(Integer, primary_key=True)
    village = Column(String(50))

    def __init__(self, village: str):
        self.village = village

    def __repr__(self):
        return f'Village(village="{self.village}")'
