import {
  Button, Form,
} from 'react-bootstrap';
import React from 'react';
import OccupationForm from './OccupationForm';
import ContactDetailsForm from './ContactDetailsForm';
import BasicsForm from './BasicsForm';
import DiagnosisForm from './DiagnosisForm';
import AddressForm from './AddressForm';

function PatientForm() {
  return (
    <div className="patient-form" style={{ width: '85%', margin: 'auto' }}>
      <Form>
        <BasicsForm />
        <OccupationForm />
        <ContactDetailsForm />
        <DiagnosisForm />
        <AddressForm />

        <Button variant="success" type="submit">
          Add Patient
        </Button>
      </Form>
      <br />
    </div>
  );
}

export default PatientForm;
