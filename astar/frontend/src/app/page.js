'use client'

import React, { Component } from 'react';
import '../css/navbar.css'
import 'bootstrap/dist/css/bootstrap.css';
import SearchResultDisplay from '../app/ResultDisplay'

class HomePage extends Component {
  render() {
    return (
      <SearchResultDisplay />
    );
  }
}

export default HomePage;