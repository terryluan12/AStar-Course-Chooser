import React, { Component, useState } from "react";
import axios from "axios"
import './LogIn.css'
import { useHistory } from "react-router-dom";
import { Redirect } from 'react-router'


class LogIn extends Component {
    

  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: "",
      login: false
    };
    this.handleLogin = this.handleLogin.bind(this);
    this.handleUsernameChange = this.handleUsernameChange.bind(this);
    this.handlePasswordChange = this.handlePasswordChange.bind(this);
  }
  

  handleUsernameChange(event) {
    console.log("in handle change");
    console.log("pass username in", event.target.value)
    this.setState({username: event.target.value})

  }

  handlePasswordChange(event) {
    console.log("in handle change");
    console.log("pass in", event.target.value)
    this.setState({password: event.target.value})

  }

  handleLogin(event) {
    console.log("handle login");
    console.log("state: ", this.state)
    event.preventDefault();
    this.createAccount(this.state.username, this.state.password)
    localStorage.setItem('username', this.state.username);

    this.props.history.push('/Wishlist');
  }

  createAccount = (username, password) => {
    axios.post(`http://localhost:5000/user/login`, {
        'username': this.state.username,
        'password': this.state.password
    })
    .then(res => {
        console.log("create status: ", res.status)
        if (res.status === 200) {
            this.setState({login: true})
            console.log("username:" , this.state.username)
            alert("Login Successfully!")
        }
        
    })
  }

  render() {
    return (
      <div className={"sign-up"}>
        <h1> Log In</h1>
        <form onSubmit={this.handleLogin}>
          <input
            name="username"
            onChange={this.handleUsernameChange}
            required
            type="text"
            placeholder="Username"
            className={"signup-input"}
          />
          <br />
          <input
            name="password"
            onChange={this.handlePasswordChange}
            required
            type="text"
            placeholder="Password"
            className={"signup-input"}
          />
          <br />
          <a href={`/?username=${this.state.username}`} style={{textDecoration: "none"}}>

            <button
                type="submit"
                className="signup-button"
                

            >
                Log In
            </button>
        </a>
        </form>      
      </div>
    );
  }
}

export default LogIn;