'use client'

import React, { Component } from 'react';
import '../css/navbar.css'
import 'bootstrap/dist/css/bootstrap.css';
import logo from '../img/logo.png'
import { Navbar, Nav } from "react-bootstrap";
import Link from 'next/link'

class NavbarComp extends Component {

  constructor(props){
    super(props)
    this.state = {
      username: undefined,
      login: false
    }
  }
  

  componentDidMount() {
    if (localStorage.getItem('username') !== "") {
      this.setState({username: localStorage.getItem('username')})
    }
  }

  logOut = () => {
    localStorage.setItem('username', "");
    this.setState({username: ""})
  }

  render() {
    return (
        <div>
          <Navbar bg="myBlue" variant="dark" sticky="top" expand="lg">
            <Navbar.Brand>
              <img src={logo} alt="" />{" "}
              <Nav.Link href="/" style={{ color: "white", display: "inline" }}>
                A* Course Finder
              </Nav.Link>
            </Navbar.Brand>

            <Navbar.Toggle />
            <Navbar.Collapse>
              <Nav>
                <Nav.Link as={Link} href="/search">
                  Search
                </Nav.Link>

                {this.state.username &&
                <Nav.Link as={Link} href="/wishlist">
                My Wishlist
              </Nav.Link>

              }


                {!this.state.username ?
                  <Nav.Link as={Link} href="/login">
                    Login
                  </Nav.Link>
                  :
                  <Nav.Link onClick={this.logOut} as={Link} href="/">
                    Logout
                  </Nav.Link>
                }


                {!this.state.username &&
                <Nav.Link as={Link} href="/signup">
                  Sign Up
                </Nav.Link>
                }

              </Nav>
            </Navbar.Collapse>
          </Navbar>
        </div>
    );
  }
}

export default NavbarComp;