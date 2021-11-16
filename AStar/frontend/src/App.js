import React, { Component, useState } from 'react'
import Navbar from 'react-bootstrap/Navbar';
import NavbarComp from "./components/Navbar.js";

import logo from './logo.svg';
import './App.css';


function App() {
  // return (
  //   <div className="App">
  //     <header className="App-header">
  //       <img src={logo} className="App-logo" alt="logo" />
  //       <p>
  //         Edit <code>src/App.js</code> and save to reload.
  //       </p>
  //     </header>
  //   </div>



  // );
  return (
    <div className="App">
      <NavbarComp />
      {/* <CourseList/> */}
    </div>
  );


}

// class ClassName {
//   constructor() {

//   }
// }

export default App;