import React, { Component } from "react";
import { Form, FormControl, Button, Table } from "react-bootstrap";
import "./css/styles.css";
import SearchResults from "./searchresults.js";
import APIService from "./APIService";
import axios from 'axios'
import Result from './Results'
import './Result.css'


class SearchResultDisplay extends Component{

  constructor() {
    super();
    this.state = {
      course_code : "",
      course_name: "",
      results: []
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    console.log(event)
    this.setState({course_code: event.target.value});
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.course_code);
    console.log("submitted")
    event.preventDefault();
    this.getData(this.state.course_code)
  }

  getData = (course) => {
    axios.get(`http://localhost:5000/SearchCourse`)
      .then(res => {
        console.log("finish search")
        console.log(res.data.course_name)
        this.setState({course_name : res.data.course_name})
    })
  }
  


  render(){
    return (
      <div className="SearchQuery">
        <div style={{ marginTop: "10%" }}>
 
            <h1> A* Course Finder Search</h1>
            <form onSubmit={this.handleSubmit} className={"search"}>
                <input placeholder={"Search for course code, course name, keyword ..."} className={"text-input"} type="text" value={this.state.course_code} onChange={this.handleChange} />
                <input type="submit" value="Submit" className={"submit-button"}/>
            </form>
        </div>

        {this.state.course_name !== "" ?
        <div className={"search-result-display"} ><Result course_code={this.state.course_code} course_name={this.state.course_name}></Result></div> : 
        <div></div>
        }
      </div>
    );
  }

}


export default SearchResultDisplay;
