import {
  Col, Form, Row,
} from 'react-bootstrap';
import React from 'react';

function OccupationForm() {
  return (
    <>
      <h5>Occupation</h5>
      <Form>
        <Form.Group as={Row} className="mb-3" controlId="formOccupationTitle">
          <Form.Label column sm={2}>Occupation Title</Form.Label>
          <Col sm={10}>
            <Form.Control placeholder="Enter occupation title" />
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="formOccupationCompany">
          <Form.Label column sm={2}>Occupation Company</Form.Label>
          <Col sm={10}>
            <Form.Control placeholder="Enter occupation company" />
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="formOccupationDescription">
          <Form.Label column sm={2}>Occupation Description</Form.Label>
          <Col sm={10}>
            <Form.Control placeholder="Enter occupation description" />
          </Col>
        </Form.Group>
      </Form>
    </>
  );
}

export default OccupationForm;
