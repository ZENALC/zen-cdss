import {
  Col, Form, Row,
} from 'react-bootstrap';
import React from 'react';
import NepalMap from './address_info/nepal_map.json';

const PROVINCES = Object.keys(NepalMap);
const DISTRICTS = (province) => Object.keys(NepalMap[province]);
const MUNICIPALITIES = (province, municipality) => NepalMap[province][municipality];

function AddressForm() {
  return (
    <>
      <h5>Address</h5>
      <Form>
        <Form.Group as={Row} className="mb-3" controlId="formAddress">
          <Form.Label column sm={2}>Address</Form.Label>
          <Col sm={10}>
            <Form.Control placeholder="Enter address" />
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="formVillage">
          <Form.Label column sm={2}>Village</Form.Label>
          <Col sm={10}>
            <Form.Control placeholder="Enter village" />
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="formProvince">
          <Form.Label column sm={2}>Province</Form.Label>
          <Col sm={10}>
            <Form.Select defaultValue="Select...">
              <option>Select...</option>
              {PROVINCES.map((province) => (<option>{province}</option>))}
            </Form.Select>
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="formDistrict">
          <Form.Label column sm={2}>District</Form.Label>
          <Col sm={10}>
            <Form.Select defaultValue="Select...">
              <option>Select...</option>
              {DISTRICTS('Province No. 1').map((district) => (<option>{district}</option>))}
            </Form.Select>
          </Col>
        </Form.Group>

        <Form.Group as={Row} className="mb-3" controlId="formMunicipality">
          <Form.Label column sm={2}>Municipality</Form.Label>
          <Col sm={10}>
            <Form.Select defaultValue="Select...">
              <option>Select...</option>
              {MUNICIPALITIES('Province No. 1', 'Taplejung').map((municipality) => (
                <option>{municipality}</option>))}
            </Form.Select>
          </Col>
        </Form.Group>
      </Form>
    </>
  );
}

export default AddressForm;
