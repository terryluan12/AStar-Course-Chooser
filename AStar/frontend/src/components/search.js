import React, { Component } from "react";
import { Form, FormControl, Button, Table } from "react-bootstrap";
//import { CourseList } from "./courselist";
import "./css/styles.css";
//import courselist from "./MOCK_DATA.json";
import SearchResults from "./searchresults.js";

function SearchQuery() {
  return (
    <div className="SearchQuery">
      <div style={{ marginTop: "20%" }}>
        <h1> A* Course Finder Search</h1>
        <Form
          style={{
            display: "flex"
          }}
        >
          <span style={{ width: "25%" }}></span>
          <FormControl
            type="text"
            placeholder="Search for course code, course name or keyword"
            className="mr-sm-2"
            style={{ width: "50%" }}
          />
          {/* should send query word, search database, return list of items and display results when search button is clicked */}
          <Button className="myButton"> Search</Button>
        </Form>
      </div>
      <SearchResults />
    </div>
  );
}
export default SearchQuery;
