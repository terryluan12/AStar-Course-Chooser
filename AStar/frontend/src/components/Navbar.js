import React, { Component, useState } from 'react';
import './css/navbar.css'
import 'bootstrap/dist/css/bootstrap.css';
import logo from './img/logo.png'
import { Navbar, Nav, Form, FormControl, Button } from "react-bootstrap";
import { BrowserRouter as Router, Route, Switch, Link, useLocation } from "react-router-dom";
import Search from "./search.js";
// import Login from "./login.js";
import LogIn from "./LogIn.jsx";
import CourseDescriptionPage from "./CourseDescription";
import Wishlist from './Wishlist';
import SignUp from './SignUp'
import SearchResultDisplay from './ResultDisplay'


function CourseDescription (props) {
  let query = useQuery();
  console.log("query: ", query.get("code"))
  return <CourseDescriptionPage code={query.get("code")} username={props.username}/>;
}

function useQuery() {
  const { search } = useLocation();
  console.log("useLocation: ", search)

  return React.useMemo(() => new URLSearchParams(search), [search]);
}

export default class NavbarComp extends Component {

  constructor(props){
    super(props)

  

  this.state={
    username: ""
    // , isLoggedIn: false
   
  }
  // this.CourseDescription = this.CourseDescription.bind(this)
  this.setUsername = this.setUsername.bind(this)
  }


  // CourseDescription =(username) =>{
  //   // function CourseDescription (username) {
  //     let query = useQuery();
  //     console.log("query: ", query.get("code"))
  //     return <CourseDescriptionPage code={query.get("code")} username={username}/>;
  //   // }
  // }

  
  

  setUsername = (username) => {
    // console.log("data retrieved: " + data[0].username + "pass:" +data[0].password)
    this.setState({
      username: username
      // , isLoggedIn: true
    })
    console.log("navbar state:", this.state)
  }

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
                <Nav.Link as={Link} to="/Wishlist">
                  My Wishlist
                </Nav.Link>

                {!this.state.username ?
                <Nav.Link 
                // onClick={this.setState({username: "aaa"})}
                as={Link} to="/login">
                  Login
                </Nav.Link>
                :
                <Nav.Link 
                onClick={this.setState({username: ""})}
                 as={Link} to="/">
                  Logout
                </Nav.Link>

                }
              
                <Nav.Link as={Link} to="/signup">
                  Sign Up
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
            <Route path="/search">
              <SearchResultDisplay />
            </Route>
          
            <Route exact
            path="/course/details"
            render={props =>(

              
              // <CourseDescriptionPage {...props} username={this.state.username}/>
              <CourseDescription {...props} username={this.state.username} />
              // <CourseDescription(this.state.username) />
              )}>
            

            </Route>
            {/* {console.log("wishlist data: ", wishlist_data)} */}
            <Route exact 
            path="/Wishlist"
              render={props =>(
                <Wishlist {...props} username={this.state.username} wishlist={this.state.wishlist_data}/>
              )}
              >
            </Route>
            {/* <Route path="/login">
              <Login />
            </Route> */}

            {/* if username is not null, login will render */}
             
            <Route exact path="/login"
                render={props => (
                  
                <LogIn {...props} setUsername={this.setUsername} 
                //  setPassword={this.setPassword}
                />
                )}
                >
     
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