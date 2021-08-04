"""
Province model.
"""

from sqlalchemy import Column, Integer, String

from backend.database.base import Base


class Province(Base):  # pylint: disable=too-few-public-methods
    """
    Province table.
    """
    __tablename__ = "province"

    id = Column(Integer, primary_key=True)
    province = Column(String(50))

    def __init__(self, province: str):
        self.province = province

    def __repr__(self):
        return f'Province(province={self.province})'
