"use client";
import React, { useState } from "react";
import axios from "axios";
import "../../css/SignUp.css";

function SignupPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleLogin = async (event) => {
    event.preventDefault();
    const res = await createAccount(username, password);
    switch (res.status) {
      case 200:
        alert("Create Account Successfully!");
        break;
      default:
        alert("Unknown Error. Please contact website owner");
        break;
    }
  };

  const createAccount = async (username, password) => {
    return await axios.post(
      `${process.env.NEXT_PUBLIC_API_URL}/user`,
      {
        username: username,
        password: password,
      },
    );
  };

  return (
    <div className={"sign-up"}>
      <h1> Sign Up</h1>
      <form onSubmit={handleLogin}>
        <input
          name="username"
          onChange={handleUsernameChange}
          required
          type="text"
          placeholder="Username"
          className={"signup-input"}
        />
        <br />
        <input
          name="password"
          onChange={handlePasswordChange}
          required
          type="text"
          placeholder="Password"
          className={"signup-input"}
        />
        <br />
        <button type="submit" className="signup-button">
          Sign Up
        </button>
      </form>
    </div>
  );
}

export default SignupPage;
