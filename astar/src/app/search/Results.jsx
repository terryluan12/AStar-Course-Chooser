'use client'
import React, { Component, useImperativeHandle } from "react";
import axios from 'axios'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row'
import Col from 'react-bootstrap/Col'
import '../../css/Result.css'
import unstarred from '../../img/star.png'
import starred from '../../img/starred.png'
import Link from 'next/link'

let star;

class Result extends Component{

  constructor(props) {
    super(props);
    this.state = {
      course_code : this.props.course_code,
      course_name: this.props.course_name,
      division: "Division of Computer Engineering",
      faculty: "Faculty of Applied Science and Engineering",
      starred: false,
      username: localStorage.getItem('username')
    };
    star = unstarred
  }

  
  componentDidMount() {
if(this.state.username){
      axios.get(`${process.env.NEXT_PUBLIC_API_URL}/user/wishlist?username=${this.state.username}`)
      .then(res => {
        let len = res.data.wishlist.course.length
        for (let i = 0; i < len; i++) {
          if (res.data.wishlist.course[i].code === this.state.course_code) {
            star = starred
            this.setState({starred: true})
          }
        }
      })
}
  }





  render(){
    return (
      <Container>
        <Link href={`/courseDetails/${this.state.course_code}`} className={"search-result-item"} style={{textDecoration: "none"}}>
        <Row className={"result-display"}>
            <Col>
                <h5>{this.state.course_code}</h5>  
            </Col>
            <Col>
                <h5>{this.state.course_name}</h5>
            </Col>
            <Col>{this.state.division}</Col>
            <Col>{this.state.faculty}</Col>
            <Col><img src={star} alt=""/></Col>
        </Row>
        </Link>
      </Container>
    );
  }
}

export default Result;
