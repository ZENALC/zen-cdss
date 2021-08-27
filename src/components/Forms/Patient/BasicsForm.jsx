import { Col, Form, Row } from 'react-bootstrap';
import React from 'react';

function BasicsForm() {
  return (
    <>
      <h5>Basics</h5>
      <Form.Group as={Row} className="mb-3" controlId="formFirstName">
        <Form.Label column sm={2}>First Name</Form.Label>
        <Col sm={10}>
          <Form.Control placeholder="Enter first name" />
        </Col>
      </Form.Group>

      <Form.Group as={Row} className="mb-3" controlId="formLastName">
        <Form.Label column sm={2}>Last Name</Form.Label>
        <Col sm={10}>
          <Form.Control placeholder="Enter last name" />
        </Col>
      </Form.Group>

      <Form.Group as={Row} className="mb-3" controlId="formGridGender">
        <Form.Label column sm={2}>Gender</Form.Label>
        <Col sm={10}>
          <Form.Select defaultValue="Select...">
            <option>Select...</option>
            <option>Male</option>
            <option>Female</option>
          </Form.Select>
        </Col>
      </Form.Group>

      <Form.Group as={Row} className="mb-3" controlId="formDateOfBirth">
        <Form.Label column sm={2}>Date of Birth</Form.Label>
        <Col sm={10}>
          <Form.Control type="date" name="dob" />
        </Col>
      </Form.Group>

      <Form.Group as={Row} className="mb-3" controlId="formRegistrationDate">
        <Form.Label column sm={2}>Registration Date</Form.Label>
        <Col sm={10}>
          <Form.Control
            type="date"
            name="registrationDate"
            value={new Date().toISOString().slice(0, 10)}
          />
        </Col>
        <small>This will default to today.</small>
      </Form.Group>

      <Form.Group as={Row} className="mb-3" controlId="formFamilyDiabetics">
        <Form.Label column sm={2}>Family Diabetics</Form.Label>
        <Col sm={10}>
          <Form.Control placeholder="Enter patient's relatives with diabetes" />
        </Col>
      </Form.Group>

      <Form.Group as={Row} className="mb-3" controlId="formReferredBy">
        <Form.Label column sm={2}>Referred By</Form.Label>
        <Col sm={10}>
          <Form.Control placeholder="Enter who referred this patient" />
        </Col>
      </Form.Group>

      <Form.Group as={Row} className="mb-3" controlId="formAccompaniedBy">
        <Form.Label column sm={2}>Accompanied By</Form.Label>
        <Col sm={10}>
          <Form.Control placeholder="Enter who accompanied this patient" />
        </Col>
      </Form.Group>
    </>
  );
}

export default BasicsForm;
