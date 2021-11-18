import React, { Component, useState } from "react";
// import { propTypes } from "react-bootstrap/esm/Image";
import { render } from "react-dom";
// import { useHistory } from "react-router-dom";
import APIService from "./APIService";
import Wishlist from "./Wishlist";
import NavbarComp from "./Navbar";
// import Routes from "../routes";
import App from "../App";
import axios from "axios";

class Login extends Component {
  // const [username, setUsername] = useState("");
  // const [password, setPassword] = useState("");

  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: ""
    };
    this.handleLogin = this.handleLogin.bind(this);
    this.handleChange = this.handleChange.bind(this);
    // this.setAccount=this.props.setAccount.bind(this);
    // this.history=useHistory()
  }

 

  // insertArticle(event) {
  //   APIService.insertArticle(this.state)
  //     .then((response) => event.insertedArticle(response))
  //     // should "event" be props?
  //     .catch((error) => console.log("error", error));
  // }


  handleChange(event) {
    console.log("in handle change");
    this.setState({
      [event.target.name]: event.target.value
    });
    console.log("login state: ", this.state)
  }

  handleLogin(event) {
    console.log("entered handle login with states: ", this.state);
    event.preventDefault();
    // alert(
    //   "you submitted: " +
    //     this.state.username +
    //     " and pass: " +
    //     this.state.password
    // );

    // const userInfo = [{username: this.state.username, password: this.state.password}]
    // const userInfo = [this.state.username, this.state.password]


    axios.post(`https://astarchooser.herokuapp.com/user/login`, {
        'username': this.state.username,
        'password': this.state.password
    })
    .then(res => {
        console.log("create status: ", res.status)
        if (res.status === 200) {
            this.setState({login: true})
            console.log("username:" , this.state.username)
            this.props.setUsername(this.state.username);
            this.props.history.push('/Wishlist');
            alert("Login Successfully!")
        }
        
    })
  }
   
  
  render() {
    return (
      <div style={{ marginTop: "20%" }}>
        <h1> Login</h1>
        <form onSubmit={this.handleLogin}>
          <input
            name="username"
            // onChange={this.handleChange}
            onChange={(e)=>this.setState({username: e.target.value})}
            required
            type="text"
            placeholder="Username"
            style={{ marginTop: "5%" }}
          />
          <br />
          <input
            name="password"
            // onChange={this.handleChange}
            onChange={(e)=>this.setState({password: e.target.value})}
            required
            type="text"
            placeholder="Password"
            style={{ marginTop: "5%" }}
          />
          <br />
          <button
            type="submit"
            className="myButton"
            style={{ marginTop: "5%" }}
          >
            Login
          </button>
        </form>

      </div>
    );
  }
}


export default Login;