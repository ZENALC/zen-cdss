"""
Miscellaneous functions to leverage to insert to the database.
"""
from typing import Any, Dict, Optional

from backend.database.base import Base, engine
from backend.database.models.address import Address, District, Municipality, Province, Village
from backend.database.models.patient import Company, ContactDetails, Diagnosis, Occupation, OccupationTitle, Patient
from backend.database.utils import session_scope, yield_helper


def create_entry(table: Base, accessor: str, value: str, existing_session=None) -> Optional[Base]:
    """
    Creates an entry in the table provided. Regardless of whether it created one or not, it will return the
    object that matches the arguments passed.
    :param table: Table to create an entry in.
    :param accessor: Accessor to filter table with.
    :param value: Value to populate the new entry with.
    :param existing_session: Preexisting session to leverage to avoid creating new sessions (if provided).
    """
    if value is None:  # If the value we are filtering against is None, then just return None as the DB will hold null.
        return None

    context_manager = session_scope if existing_session is None else lambda: yield_helper(existing_session)
    with context_manager() as session:
        result = session.query(table).filter(getattr(table, accessor) == value).all()

        if not result:  # If the resulting list is empty, then just create the table with the value provided.
            return table(value)

        return result.pop()  # Only one object should exist, so pop it off and return it.


def add_occupation(patient_dict: Dict[str, Any], patient: Patient, existing_session=None) -> Occupation:
    """
    Add occupation.
    :param patient_dict: Patient dictionary with occupation details.
    :param patient: Patient object to link occupation to.
    :param existing_session: Preexisting session to leverage to avoid creating new sessions (if provided).
    :return: Occupation object.
    """
    context_manager = session_scope if existing_session is None else lambda: yield_helper(existing_session)
    with context_manager() as session:
        description = patient_dict['occupation_description']

        occupation_title = create_entry(table=OccupationTitle,
                                        accessor='occupation_title',
                                        value=patient_dict.get('occupation_title'),
                                        existing_session=session)
        company = create_entry(table=Company,
                               accessor='company',
                               value=patient_dict.get('company'),
                               existing_session=session)

        occupation = Occupation(
            patient=patient,
            description=description,
            company=company,
            occupation_title=occupation_title
        )

        if existing_session is None:  # Only add the object if we just created the session object.
            session.add(occupation)

        return occupation


def add_patient(patient_dict: Dict[str, Any]):
    """
    Add patients through this function to the database.
    :param patient_dict: Dictionary containing patient information.
    """
    with session_scope() as session:
        patient = Patient(
            first_name=patient_dict['first_name'],
            last_name=patient_dict['last_name'],
            gender=patient_dict['gender'],
            date_of_birth=patient_dict['date_of_birth'],
            registration_date=patient_dict.get('registration_date'),
            referred_by=patient_dict.get('referred_by'),
            accompanied_by=patient_dict.get('accompanied_by'),
            family_diabetics=patient_dict.get('family_diabetics')
        )

        add_address(patient_dict=patient_dict, patient=patient, existing_session=session)
        add_contact_details(patient_dict=patient_dict, patient=patient)

        session.add(patient)


def add_contact_details(patient_dict: Dict[str, Any], patient: Patient, existing_session=None) -> ContactDetails:
    """
    Adds contact details.
    :param patient_dict: Patient dictionary with contact details.
    :param patient: Patient object to link contact details to.
    :param existing_session: Preexisting session to leverage to avoid creating new sessions (if provided).
    :return: Contact details object.
    """
    context_manager = session_scope if existing_session is None else lambda: yield_helper(existing_session)
    with context_manager() as session:
        contact_details = ContactDetails(
            email=patient_dict.get('email'),
            phone_number=patient_dict.get('phone'),
            patient=patient
        )

        if existing_session is None:  # Only add the object if we just created the session object.
            session.add(contact_details)

        return contact_details


def add_diagnosis(patient_dict: Dict[str, Any], patient: Patient, existing_session=None):
    """
    Add diagnosis.
    :param patient_dict: Patient dictionary with diagnosis data.
    :param patient: Patient object to link diagnosis details to.
    :param existing_session: Preexisting session to leverage to avoid creating new sessions (if provided).
    :return: Diagnosis object.
    """
    context_manager = session_scope if existing_session is None else lambda: yield_helper(existing_session)
    with context_manager() as session:
        diagnosis = Diagnosis(
            diagnosis=patient_dict['diagnosis'],
            advent=patient.get('diagnosis_advent'),
            patient=patient
        )

        if existing_session is None:  # Only add the object if we just created the session object.
            session.add(diagnosis)

        return diagnosis


def add_address(patient_dict: Dict[str, Any], patient: Patient, existing_session=None) -> Address:
    """
    Add address with the patient dictionary provided.
    :param patient_dict: Dictionary containing patient information.
    :param patient: Patient object to link address to.
    :param existing_session: Preexisting session to leverage to avoid creating new sessions (if provided).
    """
    context_manager = session_scope if existing_session is None else lambda: yield_helper(existing_session)
    with context_manager() as session:
        address = patient_dict['address']

        province = create_entry(Province, 'province', patient_dict.get('province'), session)
        village = create_entry(Village, 'village', patient_dict.get('village'), session)
        municipality = create_entry(Municipality, 'municipality', patient_dict.get('municipality'), session)
        district = create_entry(District, 'district', patient_dict.get('district'), session)

        address = Address(
            address=address,
            province=province,
            district=district,
            municipality=municipality,
            village=village,
            patient=patient
        )

        if existing_session is None:  # Only add the object if we just created the session object.
            session.add(address)

        return address


# Generating the database schema.
Base.metadata.create_all(engine)
p_dict = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'date_of_birth': 'May 13 1992',
    'village': "some village",
    'province': 'some province',
    'address': "some address",
    'email': 'john@gmail.com',
    'phone': '7819991231'
}

add_patient(p_dict)
