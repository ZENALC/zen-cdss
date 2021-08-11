import {
  Container, Nav, Navbar, NavDropdown,
} from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';
import React from 'react';

function MainNavbar() {
  return (
    <Navbar expand="lg" variant="dark" bg="dark">
      <Container>
        <LinkContainer to="/home">
          <Navbar.Brand>ZEN CDSS</Navbar.Brand>
        </LinkContainer>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto">
            <LinkContainer to="/home">
              <Nav.Link>Home</Nav.Link>
            </LinkContainer>
            <NavDropdown title="Patient" id="basic-nav-dropdown">
              <LinkContainer to="/add_patient">
                <NavDropdown.Item>Add</NavDropdown.Item>
              </LinkContainer>
              <LinkContainer to="/view_patient">
                <NavDropdown.Item>View</NavDropdown.Item>
              </LinkContainer>
              <LinkContainer to="/import_patient">
                <NavDropdown.Item>Import</NavDropdown.Item>
              </LinkContainer>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default MainNavbar;
