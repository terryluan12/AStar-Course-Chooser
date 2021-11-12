import React, { Component } from "react";
import { Form, FormControl, Button, Table } from "react-bootstrap";
//import { CourseList } from "./courselist";
import "./css/styles.css";
//import courselist from "./MOCK_DATA.json";
import SearchResults from "./searchresults.js";
import APIService from "./APIService";


class SearchQuery extends Component{

  constructor() {
    super();
    this.state = {
      query: ""
    };
    this.handleQuery = this.handleQuery.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  postQuery(event) {
    APIService.postQuery(this.state.query)
      .then((response) => event.postQuery(response))
      // should "event" be props?
      .catch((error) => console.log("error", error));
  }

  handleChange(event) {
    console.log("in handle change");
    this.setState({
      [event.target.name]: event.target.value
    });
  }

  handleQuery(event) {
    console.log("entered here");
    event.preventDefault();
    this.postQuery(event);
    alert(
      "you submitted: " +
        this.state.query
    );
  }


  render(){
    return (
      <div className="SearchQuery">
        <div style={{ marginTop: "10%" }}>
 
          <h1> A* Course Finder Search</h1>
          <Form
            style={{
              display: "flex"
            }}
            onSubmit={this.handleQuery}
          >
            <span style={{ width: "25%" }}></span>
            <FormControl
              type="text"
              name="query"
              placeholder="Search for course code, course name or keyword"
              className="mr-sm-2"
              style={{ width: "50%" }}
              onChange={this.handleChange}
              required
            />
            {/* should send query word, search database, return list of items and display results when search button is clicked */}
            <Button type="submit" className="myButton"> Search</Button>
          </Form>
        </div>
        <SearchResults />
      </div>
    );
  }

}


export default SearchQuery;
