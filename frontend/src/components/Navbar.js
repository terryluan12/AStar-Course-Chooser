import React, { Component } from 'react';
import './css/navbar.css'
import 'bootstrap/dist/css/bootstrap.css';
import logo from './img/logo.png'

class Navbar extends Component {

	render() {
		return(

      <nav class="navbar navbar-expand justify-content-center">
        <a class="navbar-brand" href="index.html">
          <img src={logo} alt="logo"></img>
        </a>
        <div class="collapse navbar-collapse">

          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link active" href="">Search</a>
            </li>
            <li class="nav-item ms-auto">
              <a class="nav-link" href="">My Wishlist</a>
            </li>
            <li class="nav-item ms-auto">
              <a class="nav-link" href="">Log In</a>
            </li>
          </ul>
        </div>
      </nav>

		)
	}
}

export default Navbar
