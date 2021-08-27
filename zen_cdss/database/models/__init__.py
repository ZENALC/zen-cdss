"""
Initialization by importing all models.
"""

from zen_cdss.database.models.address import Address
from zen_cdss.database.models.company import Company
from zen_cdss.database.models.contact_details import ContactDetails
from zen_cdss.database.models.diagnosis import Diagnosis
from zen_cdss.database.models.district import District
from zen_cdss.database.models.municipality import Municipality
from zen_cdss.database.models.occupation import Occupation
from zen_cdss.database.models.occupation_title import OccupationTitle
from zen_cdss.database.models.patient import Patient
from zen_cdss.database.models.province import Province
from zen_cdss.database.models.village import Village

__all__ = ['Address', 'Company', 'ContactDetails', 'Diagnosis', 'District', 'Municipality', 'Occupation',
           'OccupationTitle', 'Patient', 'Province', 'Village']
