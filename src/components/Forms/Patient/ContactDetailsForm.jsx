import {
  Col, Form, Row,
} from 'react-bootstrap';
import React from 'react';

function ContactDetailsForm() {
  return (
    <>
      <h5>Contact Details</h5>
      <Form>
        <Form.Group as={Row} className="mb-3" controlId="formPhoneNumber">
          <Form.Label column sm={2}>Phone Number</Form.Label>
          <Col sm={10}>
            <Form.Control placeholder="Enter phone number" />
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="formEmail">
          <Form.Label column sm={2}>Email</Form.Label>
          <Col sm={10}>
            <Form.Control placeholder="Enter email" />
          </Col>
        </Form.Group>
      </Form>
    </>
  );
}

export default ContactDetailsForm;
