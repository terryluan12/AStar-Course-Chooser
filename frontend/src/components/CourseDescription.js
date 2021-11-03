import React, { Component } from 'react';
import './css/course-description.css'
import 'bootstrap/dist/css/bootstrap.css';
import Container from 'react-bootstrap/Container';
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'

import empty_star from './img/star.png'
import starred from './img/starred.png'
import expand_button from './img/expand-button.png'

let star = empty_star;

class CourseDescriptionPage extends Component {

  state = {
    course_code: "ECE444H1S",
    course_name: "Software Engineering",
    division: "Faculty of Applied Science and Engineering",
    department: "Department of Edward S. Rogers Sr. Dept. of Electrical & Computer Engineering",
    minor : "",
    course_description: "The software development process. Software requirements and specifications. Software design techniques. Techniques for developing large software systems; CASE tools and software development environments. Software testing, documentation and maintenance.",
    syllabus: "https://shuiblue.github.io/UofT-ECE444/",
    requisites: {
      prerequisites: "ECE344H1 or ECE355H1",
      corequisites: "",
      exclusions: "ECE344"
    },
    starred: false
  }

  check_star = () => {
    if (this.state.starred == false) {
      this.setState({starred: true});
      console.log('Starred the course');
      star = starred;

    } else {
      this.setState({starred: false});
      console.log('Unstar the course');
      star = empty_star;
    }
  }

  openLink = () => {
    const newWindow = window.open(this.state.syllabus, '_blacnk', 'noopener,noreferrer');
    if (newWindow) {
      newWindow.opener = null;
    }
  }

	render() {
		return(

      <div className="page-content">
        <Container className="course-template">
          <Row float="center" className="course-title">
            <Col xs={8}>
              <h1>{this.state.course_code} : {this.state.course_name}</h1>
            </Col>
            <Col xs={4}>
              <img src={star} onClick={this.check_star}></img>
            </Col>
          </Row>
          <Row>
            <Col className="col-item">
              <h3>Division</h3>
              <p>{this.state.division}</p>
            </Col>
            <Col className="col-item">
              <h3>Department</h3>
              <p>{this.state.department}</p>
            </Col>
            <Col>
              <Row className="col-item">
                <h4>Minor</h4>
                <p>{this.state.minor}</p>
              </Row>
              <a href={this.state.syllabus} target="_blank" className="syllabus-link">
                <Row className="col-item syllabus">
                  <h4>View Syllabus</h4>
                </Row>
              </a>
            </Col>
          </Row>
          <Row className="col-item course-description">
            <h3>Course Description</h3>
            <p>{this.state.course_description}</p>
          </Row>
          <Row className="col-item course-requisite">
            <Row>
              <h3>Course Requisites</h3>
            </Row>
            <Row>
              <Col className="requisites-display">
                <h4>Pre-Requisites</h4>
                <p>{this.state.requisites.prerequisites}</p>
              </Col>
              <Col className="requisites-display">
                <h4>Co-Requisites</h4>
                <p>{this.state.requisites.corequisites}</p>
              </Col>
              <Col className="requisites-display">
                <h4>Exclusion</h4>
                <p>{this.state.requisites.exclusions}</p>
              </Col>
            </Row>
          </Row>
          <Row>
            <Col className="text-center center-block">
              <img src={expand_button} className="expand_button"></img>
            </Col>
          </Row>
        </Container>
      </div>

		)
	}
}

export default CourseDescriptionPage
