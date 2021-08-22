import {
  Button, Col, Form, Row,
} from 'react-bootstrap';
import React from 'react';

function PatientForm() {
  return (
    <div className="patient-form" style={{ width: '85%', margin: 'auto' }}>

      <Form>

        <h5>Basic Information</h5>

        <Row className="mb-3">
          <Form.Group as={Col} controlId="formGridFirstName">
            <Form.Label>First Name</Form.Label>
            <Form.Control placeholder="Enter first name" />
          </Form.Group>

          <Form.Group as={Col} controlId="formGridLastName">
            <Form.Label>Last Name</Form.Label>
            <Form.Control placeholder="Enter last name" />
          </Form.Group>
        </Row>

        <Row className="mb-3">
          <Form.Group as={Col} controlId="formGridGender">
            <Form.Label>Gender</Form.Label>
            <Form.Select defaultValue="Select...">
              <option>Select...</option>
              <option>Male</option>
              <option>Female</option>
            </Form.Select>
          </Form.Group>

          <Form.Group as={Col} controlId="formDateOfBirth">
            <Form.Label>Date of Birth</Form.Label>
            <Form.Control type="date" name="dob" />
          </Form.Group>

          <Form.Group as={Col} controlId="formRegistrationDate">
            <Form.Label>Registration Date</Form.Label>
            <Form.Control type="date" name="registrationDate" />
          </Form.Group>
        </Row>

        <Row className="mb-3">
          <Form.Group as={Col} controlId="formFamilyDiabetics">
            <Form.Label>Family Diabetics</Form.Label>
            <Form.Control placeholder="Enter relatives with diabetes" />
          </Form.Group>

          <Form.Group as={Col} controlId="formReferredBy">
            <Form.Label>Referred By</Form.Label>
            <Form.Control placeholder="Enter who referred this patient" />
          </Form.Group>

          <Form.Group as={Col} controlId="formAccompaniedBy">
            <Form.Label>Accompanied By</Form.Label>
            <Form.Control placeholder="Enter who accompanied this patient" />
          </Form.Group>
        </Row>

        <Button variant="success" type="submit">
          Add Patient
        </Button>
      </Form>
    </div>
  );
}

export default PatientForm;
