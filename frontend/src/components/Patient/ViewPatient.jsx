import React from 'react';

import { Autocomplete } from '@material-ui/lab';
import { TextField } from '@material-ui/core';

function ViewPatient() {
  return (
    <>
      <br />
      <h3>View Patient</h3>
      <div style={{ width: '75%', margin: 'auto' }}>
        <Autocomplete
          id="patients-combobox"
          options={['Johnathan', 'Mihir']}
          getOptionLabel={(option) => option}
          renderInput={(params) => (
            <TextField /* eslint-disable-next-line react/jsx-props-no-spreading */
              {...params}
              label="Find Patient"
              variant="standard"
            />
          )}
        />
      </div>
      <hr />
      <p>No patient selected yet.</p>
    </>
  );
}

export default ViewPatient;
