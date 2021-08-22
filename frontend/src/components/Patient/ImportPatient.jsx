import React from 'react';
import { Button } from 'react-bootstrap';

function ImportPatient() {
  return (
    <>
      <br />
      <h3>Import Patient/Patients</h3>
      <p>Please upload a CSV containing patient information to import patients.</p>
      <input type="file" />
      <Button variant="success">Import</Button>
      <hr />
      <p>No imports in progress.</p>
    </>
  );
}

export default ImportPatient;
