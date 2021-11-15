import React, { Component, useState } from "react";
// import { propTypes } from "react-bootstrap/esm/Image";
import { render } from "react-dom";
// import { useState } from "react-router-dom";
import APIService from "./APIService";

class Login extends Component {
  // const [username, setUsername] = useState("");
  // const [password, setPassword] = useState("");

  constructor() {
    super();
    this.state = {
      username: "",
      password: ""
    };
    this.handleLogin = this.handleLogin.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  insertArticle(event) {
    APIService.insertArticle(this.state)
      .then((response) => event.insertedArticle(response))
      // should "event" be props?
      .catch((error) => console.log("error", error));
  }

  handleChange(event) {
    console.log("in handle change");
    this.setState({
      [event.target.name]: event.target.value
    });
  }

  handleLogin(event) {
    console.log("entered here");
    event.preventDefault();
    // this.insertArticle(event); --> needs to be
    this.insertArticle(event)
    // alert(
    //   "you submitted: " +
    //     this.state.username +
    //     " and pass: " +
    //     this.state.password
    // );
  }
  render() {
    return (
      <div style={{ marginTop: "20%" }}>
        <h1> Login</h1>
        <form onSubmit={this.handleLogin}>
          <input
            name="username"
            onChange={this.handleChange}
            required
            type="text"
            placeholder="Username"
            style={{ marginTop: "5%" }}
          />
          <br />
          <input
            name="password"
            onChange={this.handleChange}
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

        {/* <h1>
          {" "}
          username: {this.state.username} pass: {this.state.password}
        </h1> */}
      </div>
    );
  }
}

export default Login;
