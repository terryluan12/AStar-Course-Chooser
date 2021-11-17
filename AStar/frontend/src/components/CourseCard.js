import React, { Component } from "react";
import { Form, FormControl } from "react-bootstrap";
import "./css/coursecard.css";
import "bootstrap/dist/css/bootstrap.css";
// import wishlist_data from "../db/Wishlist_MOCK_data.json";
import Col from 'react-bootstrap/Col'
import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";
import ListGroupItem from "react-bootstrap/ListGroupItem";

// this function should:
// receive  a list of courses called wishlist_data from the database
// send modified comments to database. database saves it. the page rerenders to show the modified information

class CourseCard extends Component{

  constructor(props){
    super(props)
  }

  render(){
    return (

    <div className={"course-card-render"}>

      {this.props.wishlist_data.map((course)=>(
        <a href={`/course/details?code=${course.code}`} className={"wishlist-link"}>
          <Col className={"text-center wishlist-card"}>
            <h5>
              {course.code}: {course.name}
            </h5>
          </Col>
        </a>






      )



      )}
       
    </div>


    )
    
  }
}


export default CourseCard;
