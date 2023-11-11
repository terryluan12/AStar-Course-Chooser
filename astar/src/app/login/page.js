'use client'
import React, { useState } from "react";
import { useHistory } from "react-router";
import Link from 'next/link'
import axios from "axios"
import '../../css/LogIn.css'

function LoginPage(props) {
    
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [login, setLogin] = useState(false)
  const history = useHistory()

  const handleUsernameChange = (event) => {
    setUsername(event.target.value)
  }

  const handlePasswordChange = (event) => {
    setPassword(event.target.value)
  }

  const handleLogin = async (event) => {
    event.preventDefault();
    const res = await loginAccount(username, password)
    console.log("AI IT IS ", res)
    switch(res.status){
      case 200:
        setLogin(true)
        localStorage.setItem('username', username);
        history.push('/Wishlist');    
        break
      default:
        alert("Invalid Username and Password. Please try again")
        break
      }
  }
  const loginAccount = async (username, password) => {
    console.log("ILLLL, IT IS ", username, password)
    return await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/user/login`, {
        'username': username,
        'password': password
    })
  }

  return (
    <div className={"sign-up"}>
      <h1> Log In</h1>
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
        <Link href={`?username=${username}`} style={{textDecoration: "none"}} className="signup-button">
          <button type="submit" onClick={handleLogin}>
              Log In
          </button>
        </Link>
      </form>      
    </div>
  );
}

export default LoginPage;