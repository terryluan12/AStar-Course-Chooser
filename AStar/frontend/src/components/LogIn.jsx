import React, { Component } from "react";
import axios from "axios"
import './LogIn.css'

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
    this.setState({username: event.target.value})
  }

  handlePasswordChange(event) {
    this.setState({password: event.target.value})
  }

  handleLogin(event) {
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
        if (res.status === 200) {
            this.setState({login: true})
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
            <button type="submit" className="signup-button">
                Log In
            </button>
          </a>
        </form>      
      </div>
    );
  }
}

export default LogIn;