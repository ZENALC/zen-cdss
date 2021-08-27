"""
Occupation title model.
"""

from sqlalchemy import Column, Integer, String

from zen_cdss.database.base import Base


class OccupationTitle(Base):  # pylint: disable=too-few-public-methods
    """
    Occupation title.
    """
    __tablename__ = "occupation_title"

    id = Column(Integer, primary_key=True)
    occupation_title = Column(String)

    def __init__(self, occupation_title: str):
        self.occupation_title = occupation_title

    def __repr__(self):
        return f'OccupationTitle(occupation_title="{self.occupation_title}")'
