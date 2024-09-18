"use client";
import React, { useState } from "react";
import { useRouter } from 'next/navigation'
import { signupAccount } from "@/api.js";
import "@/css/SignUp.css";

function SignupPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter()

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleLogin = async (event) => {
    event.preventDefault();
    const res = await createAccount(username, password)
    alert(res.data.message)
    if (res.status === 201) {
      localStorage.setItem("username", username);
      router.push('/wishlist')
    }
  };

  const createAccount = async (username, password) => {
    let response = null
    await signupAccount(username, password).then((res) => {
      response = res;
    }).catch((err) => {
      response = err.response;
    });
    return response;
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
          type="password"
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
