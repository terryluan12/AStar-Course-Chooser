import React, { Component } from 'react';
import './css/course-description.css'
import 'bootstrap/dist/css/bootstrap.css';
import Container from 'react-bootstrap/Container';
import Col from 'react-bootstrap/Col'
import Row from 'react-bootstrap/Row'

import empty_star from './img/star.png'
import starred from './img/starred.png'
import expand_button from './img/expand-button.png'
import axios from "axios"

let star = empty_star;

class CourseDescriptionPage extends Component {

  constructor(props){
    super(props)

    this.state = {
      course_code: "",
      // course_code: "ECE568H1",
      course_name: "",
      division: "Faculty of Applied Science and Engineering",
      department: "Department of Edward S. Rogers Sr. Dept. of Electrical & Computer Engineering",
      minor : "",
      course_description: "",
      syllabus: "",
      prerequisites: "",
      corequisites: "",
      exclusions: "",
      starred: false,
      // username:"aaa"
      username: localStorage.getItem('username')
    }
  }

  

  componentDidMount() {
    console.log("props: ", this.props.code)

    axios.get(`http://localhost:5000/course/details?code=${this.props.code}`, {
      code: this.props.course_code
    })
      .then(res => {
        console.log(res.data)
        this.setState({course_code: res.data.course.code})
        this.setState({course_name: res.data.course.name})
        this.setState({course_description : res.data.course.description})
        let prereq_len = res.data.course.prereq.length
        if (prereq_len > 1) {
          let prereq_str = ""
          for (let i = 0; i < prereq_len; i++) {
            prereq_str += res.data.course.prereq[i] 
            if (i != prereq_len - 1) {
              prereq_str += ", "
            }
          }
          this.setState({prerequisites : prereq_str})
        } else {
          this.setState({prerequisites : res.data.course.prereq})
        }
        let coreq_len = res.data.course.coreq.length
        if (coreq_len > 1) {
          let coreq_str = ""
          for (let i = 0; i < coreq_str; i++) {
            coreq_str += res.data.course.coreq[i] 
            if (i != coreq_len - 1) {
              coreq_str += ", "
            }
          }
          this.setState({corequisites : coreq_str})
        } else {
          this.setState({corequisites : res.data.course.coreq})
        }
        let exclusion_len = res.data.course.exclusion.length
        if (exclusion_len > 1) {
          let exclusion_str = ""
          for (let i = 0; i < exclusion_str; i++) {
            exclusion_str += res.data.course.exclusion[i] 
            if (i != exclusion_len - 1) {
              exclusion_str += ", "
            }
          }
          this.setState({exclusions : exclusion_str})
        } else {
          this.setState({exclusions : res.data.course.exclusion})
        }
        let syllabus_link = "http://courses.skule.ca/course/" + this.props.code + "H1"
        this.setState({syllabus : syllabus_link})

        
    })
  
    console.log("new state: ", this.state)
  }

  check_star = () => {

    console.log("username: ", this.state.username)

    // if (this.props.username){
    if(this.state.username){
      if (this.state.starred == false) { //if user is logged in, add to course
        
         
        //add course to wishlist
        console.log("username/code", this.state)
        axios.post(`http://localhost:5000/user/wishlist/addCourse?username=${this.state.username}&code=${this.state.course_code}`, {
          'code': this.state.course_code, 'username':this.state.username
        })
        .then(resp =>{
          if(resp.status == 200){
            console.log("successfully added course and starred")
            star = starred;
            this.setState({starred: true});

          }else{
            console.log("error occured while modifying wishlist: ", resp.status)
          }


        })

      } else {
        
        //remove course from wishlist
        axios.post(`http://localhost:5000/user/wishlist/removeCourse?username=${this.state.username}&code=${this.state.course_code}`, {
          'code': this.state.course_code, 'username':this.state.username
        })
        .then(resp =>{
          if(resp.status==200){
            console.log("successfully REMOVED course and unstarred")
            star = empty_star;
            this.setState({starred: false});
          }else{
            console.log("error occured while modifying wishlist: ", resp.status)
          }

        })

       
        
      }

      }else{ //else, notify
        alert("You must login to save a course.")
      }
      
  }

  openLink = () => {
    const newWindow = window.open(this.state.syllabus, '_blacnk', 'noopener,noreferrer');
    if (newWindow) {
      newWindow.opener = null;
    }
  }

	render() {
    console.log('render state:', this.state)
    console.log('coursedesp state: ', this.props)
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
                <p>{this.state.prerequisites}</p>
              </Col>
              <Col className="requisites-display">
                <h4>Co-Requisites</h4>
                <p>{this.state.corequisites}</p>
              </Col>
              <Col className="requisites-display">
                <h4>Exclusion</h4>
                <p>{this.state.exclusions}</p>
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
