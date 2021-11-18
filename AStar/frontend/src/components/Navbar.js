import React, { Component } from 'react';
import './css/navbar.css'
import 'bootstrap/dist/css/bootstrap.css';
import logo from './img/logo.png'
import { Navbar, Nav } from "react-bootstrap";
import { BrowserRouter as Router, Route, Switch, Link, useLocation } from "react-router-dom";
import LogIn from "./LogIn.jsx";
import CourseDescriptionPage from "./CourseDescription";
import Wishlist from './Wishlist';
import SignUp from './SignUp'
import SearchResultDisplay from './ResultDisplay'

function CourseDescription (props) {
  let query = useQuery();
  console.log("navbar call course description")
  return <CourseDescriptionPage code={query.get("code")} />;
}

function useQuery() {
  const { search } = useLocation();

  return React.useMemo(() => new URLSearchParams(search), [search]);
}


export default class NavbarComp extends Component {

  constructor(props){
    super(props)
    this.state = {
      username: localStorage.getItem('username'),
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
      <Router>
        <div>
          <Navbar bg="myBlue" variant="dark" sticky="top" expand="lg">
            <Navbar.Brand>
              <img src={logo} />{" "}
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
                
                {this.state.username !== "" &&
                <Nav.Link as={Link} to="/Wishlist">
                My Wishlist
              </Nav.Link>
                
              }
                

                {this.state.username === "" ?
                  <Nav.Link as={Link} to="/login">
                    Login
                  </Nav.Link>
                  :
                  <Nav.Link onClick={this.logOut} as={Link} to="/">
                    Logout
                  </Nav.Link>
                }


                {this.state.username === "" &&
                <Nav.Link as={Link} to="/signup">
                  Sign Up
                </Nav.Link>
                }
                
              </Nav>
            </Navbar.Collapse>
          </Navbar>
        </div>
        <div>
          <Switch>
            <Route path="/search">
              <SearchResultDisplay />
            </Route>
            <Route exact
              path="/course/details"
              render={props =>(<CourseDescription {...props} />)}>
            </Route>
            <Route exact 
              path="/Wishlist"
              render={props =>(
                <Wishlist {...props} wishlist={this.state.wishlist_data}/>
              )}>
            </Route>
            <Route exact path="/login"
                render={props => (
                  <LogIn {...props} />
                )}>
            </Route>
            <Route path="/signup">
              <SignUp />
            </Route>
            <Route path="/">
              <SearchResultDisplay />
            </Route>
          </Switch>
        </div>
      </Router>
    );
  }
}