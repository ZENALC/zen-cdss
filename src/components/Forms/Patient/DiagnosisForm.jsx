import {
  Col, Form, Row,
} from 'react-bootstrap';
import React from 'react';

function DiagnosisForm() {
  return (
    <>
      <h5>Diagnosis</h5>
      <Form>
        <Form.Group as={Row} className="mb-3" controlId="formDiagnosis">
          <Form.Label column sm={2}>Diagnosis</Form.Label>
          <Col sm={10}>
            <Form.Control placeholder="Enter diagnosis" />
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="formDiagnosisAdvent">
          <Form.Label column sm={2}>Diagnosis Advent</Form.Label>
          <Col sm={10}>
            <Form.Control type="date" name="diagnosisAdvent" />
          </Col>
        </Form.Group>
      </Form>
    </>
  );
}

export default DiagnosisForm;
