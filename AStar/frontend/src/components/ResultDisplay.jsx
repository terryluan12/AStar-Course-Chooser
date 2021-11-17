import React, { Component } from "react";
import { Form, FormControl, Button, Table } from "react-bootstrap";
import "./css/styles.css";
import SearchResults from "./searchresults.js";
import APIService from "./APIService";
import axios from 'axios'
import Result from './Results'
import './Result.css'
import Label from './Label'


class SearchResultDisplay extends Component{

  constructor() {
    super();
    this.state = {
      input: "",
      course_code : "",
      course_name: "",
      code: [],
      name: [],
      results: []
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    console.log(event)
    this.setState({input: event.target.value});
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.input);
    console.log("submitted")
    event.preventDefault();
    this.getData(this.state.input)
  }

  getData = (input) => {
    axios.get(`http://localhost:5000/search?input=${input}`)
      .then(res => {
        console.log("finish search")
        console.log("return data: ",res.data)

        if (res.data.length > 0) {
            let len = res.data.length
            let result_temp = []
            let name_temp = []
            let code_temp = []
            result_temp.push(<Label></Label>)
            for (let i = 0; i < len; i++) {
                code_temp.push(res.data[i].code)
                name_temp.push(res.data[i].name)
                result_temp.push(<Result course_code={res.data[i].code} course_name={res.data[i].name}></Result>)
                console.log(res.data[i].code)
            }
            console.log(result_temp)
            console.log("code temp: ", code_temp)
            this.setState({code: code_temp})
            this.setState({name: name_temp})
            this.setState({results: result_temp})
        } else {
          let result_temp = []
          console.log("res: ", res.data)
          result_temp.push(<Label></Label>)
          this.setState({code: res.data.course.code})
          this.setState({name: res.data.course.name})
          result_temp.push(<Result course_code={res.data.course.code} course_name={res.data.course.name}></Result>)
          this.setState({results: result_temp})
        }

        
        console.log("result:", this.state.results)
    })
  }
  


  render(){
    return (
      <div className="SearchQuery">
        <div style={{ marginTop: "10%" }}>
 
            <h1> A* Course Finder Search</h1>
            <form onSubmit={this.handleSubmit} className={"search"}>
                <input placeholder={"Search for course code, course name, keyword ..."} className={"text-input"} type="text" value={this.state.input} onChange={this.handleChange} />
                <input type="submit" value="Submit" className={"submit-button"}/>
            </form>
        </div>

        <div className={"search-result-display"} >
            {this.state.results}
        </div>
        
      </div>
    );
  }

}


export default SearchResultDisplay;
