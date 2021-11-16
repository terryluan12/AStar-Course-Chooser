import React, { Component } from "react";
import "./css/styles.css";
import SearchResults from "./searchresults.js";
import APIService from "./APIService";
import axios from 'axios'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import './Result.css'

import unstarred from './img/star.png'
import starred from './img/starred.png'
let star;


class Result extends Component{

  constructor(props) {
    super(props);
    this.state = {
      course_code : this.props.course_code,
      course_name: this.props.course_name,
      division: "Division of Computer Engineering",
      faculty: "Faculty of Applied Science and Engineering",
      starred: false
    };
    if (this.state.starred == false) {
        star = unstarred
    } else {
        star = starred
    }
  }

  setStar = () => {
      if (this.state.starred === false) {
          console.log("starred the course")
          this.setState({starred : true})
          star = starred
          console.log("state: ", this.state.starred)
      } else {
          console.log("unstarred the course")
          this.setState({starred : false})
          star = unstarred
          console.log("state: ", this.state.starred)
          
      }
  }


  render(){
    return (
      <Container>
        <a href={`/course/details?code=${this.props.course_code}`} className={"search-result-item"} style={{textDecoration: "none"}}>
        <Row className={"result-display"}>
            <Col>
                <h5>{this.state.course_code}</h5>  
            </Col>
            <Col>
                <h5>{this.state.course_name}</h5>
            </Col>
            <Col>{this.state.division}</Col>
            <Col>{this.state.faculty}</Col>
            <Col><img src={star} onClick={this.setStar}></img></Col>
        </Row>
        </a>
      </Container>
    );
  }

}


export default Result;
