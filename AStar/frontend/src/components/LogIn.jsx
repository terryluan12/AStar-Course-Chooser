import React, { Component } from "react";
import axios from "axios"
import './css/LogIn.css'

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
  }
  createAccount = (username, password) => {
    

    
    axios.post(`https://astarchooser.herokuapp.com/user/login`, {
        'username': this.state.username,
        'password': this.state.password
    })
    .then(res => {
        if (res.status === 200) {            
            this.setState({login: true})
            localStorage.setItem('username', this.state.username);
            this.props.history.push('/Wishlist');    
        }
        
    })
    .catch(function (error) {
      alert("Invalid Username and Password. Please try again")
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