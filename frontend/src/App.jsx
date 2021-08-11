import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom';
import MainNavbar from './components/Navbar';
import logo from './logo.svg';
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
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Edit src/App.jsx and save to reload.</p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
