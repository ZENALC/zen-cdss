import {
  Container, Nav, Navbar, NavDropdown,
} from 'react-bootstrap';
import React from 'react';

function MainNavbar() {
  return (
    <Navbar expand="lg" variant="dark" bg="dark">
      <Container>
        <Navbar.Brand href="#home">ZEN CDSS</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <NavDropdown title="Patient" id="basic-nav-dropdown">
              <NavDropdown.Item>Add</NavDropdown.Item>
              <NavDropdown.Item>Search</NavDropdown.Item>
              <NavDropdown.Item>Import</NavDropdown.Item>
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default MainNavbar;
