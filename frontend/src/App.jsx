import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom';
import MainNavbar from './components/Navbar';
import './App.css';
import AddPatient from './components/Patient/AddPatient';
import ViewPatient from './components/Patient/ViewPatient';
import ImportPatient from './components/Patient/ImportPatient';
import Home from './components/Home';

function App() {
  return (
    <div className="App">
      <Router>
        <MainNavbar />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/add_patient" component={AddPatient} />
          <Route exact path="/import_patient" component={ImportPatient} />
          <Route exact path="/view_patient" component={ViewPatient} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
