import React, { Component } from 'react';
import './css/navbar.css'
import 'bootstrap/dist/css/bootstrap.css';
import logo from './img/logo.png'
import { Navbar, Nav, Form, FormControl, Button } from "react-bootstrap";
import { BrowserRouter as Router, Route, Switch, Link, useLocation } from "react-router-dom";
import Search from "./search.js";
import SearchResults from "./searchresults";
import Login from "./login.js";
import CourseDescriptionPage from "./CourseDescription";
import Wishlist from './Wishlist';
import Result from './Results'
import SearchResultDisplay from './ResultDisplay'

function CourseDescription () {
  let query = useQuery();
  console.log("query: ", query.get("code"))
  return <CourseDescriptionPage code={query.get("code")}/>;
}

function useQuery() {
  const { search } = useLocation();
  console.log("useLocation: ", search)

  return React.useMemo(() => new URLSearchParams(search), [search]);
}

export default class NavbarComp extends Component {
  render() {
    return (
      <Router>
        <div>
          <Navbar bg="myBlue" variant="dark" sticky="top" expand="lg">
            <Navbar.Brand>
              <img src={logo} style={{ height: 53, width: 36 }} />{" "}
              <Nav.Link href="/" style={{ color: "white", display: "inline" }}>
                A* Course Finder
              </Nav.Link>
            </Navbar.Brand>

            <Navbar.Toggle />
            <Navbar.Collapse>
              <Nav>
                <Nav.Link as={Link} to="/search">
                  Search
                </Nav.Link>
                <Nav.Link as={Link} to="/searchresults">
                  Search Results (remove later)
                </Nav.Link>
                <Nav.Link as={Link} to="/MyWishlist">
                  My Wishlist
                </Nav.Link>
                <Nav.Link as={Link} to="/login">
                  Login
                </Nav.Link>
                <Nav.Link as={Link} to="/CourseDescription">
                  CourseDescription (remove later)
                </Nav.Link>
                
              </Nav>
            </Navbar.Collapse>
          </Navbar>
        </div>
        <div>
          <Switch>
            <Route path="/searchresults">
              <SearchResultDisplay />
            </Route>
            <Route path="/CourseDescription">
              <CourseDescription />
            </Route>
            <Route path="/MyWishlist">
              <Wishlist />
            </Route>
            <Route path="/login">
              <Login />
            </Route>
            <Route path="/">
              <Search />
            </Route>
            {/* <Route path="/jean_index.js">
              <Home2 />
            </Route> */}
          </Switch>
        </div>
      </Router>
    );
  }
}