import React, { Component } from 'react';
import './css/wishlist.css';
import 'bootstrap/dist/css/bootstrap.css';
import Container from 'react-bootstrap/Container';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
import Dropdown from 'react-bootstrap/Dropdown';
import { Form, FormControl } from "react-bootstrap";

import user_profile from './img/user.png'
import minor_label from './img/label.png'


import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";
import ListGroupItem from "react-bootstrap/ListGroupItem";
import CourseCard from "./CourseCard";

import courselist from "../db/MOCK_DATA.json";
import APIService from "./APIService";
import wishlist_data2 from "../db/Wishlist_MOCK_data.json";
import axios from "axios"

class Wishlist extends Component {

    constructor(props){
        super(props)

        this.state={
            wishlist_data:[],
            username: localStorage.getItem('username')
        }
    }

    componentDidMount() {
        console.log("props: ", this.props.code)

        this.setState({username: localStorage.getItem('username')})
        console.log("wishlist username: ", this.state.username )

    
        axios.get(`http://localhost:5000/user/wishlist?username=${this.state.username}`, {
            'username': this.state.username
        })
          .then(res => {
            console.log("wishlit", res.data.wishlist)
            console.log("res: ", res)

            if(res.status ==200){
                this.setState({wishlist_data: res.data.wishlist.course})
                console.log("wishlist saved: ", this.state.wishlist_data)
            }
            else{
                console.log("Error Returning Wishlist_data")
                return []
            }
    
        })
      
        console.log("new state: ", this.state)
      }

    
	render() {
		return(

            <div className="wishlist-page-content">
                <div className="left-panel">
                <h1 className="wishlist-title">My Wishlist</h1>          
                <CourseCard className={"course-card-container"} wishlist_data={this.state.wishlist_data}></CourseCard>

                </div>
                <div className="right-panel">
                    <div className="centered">
                        <img src={user_profile}></img>
                        <h3>{this.state.username}</h3>
                        <p>Computer Engineering Student</p>
                        <br></br>
                        <br></br>
                        <h4>Minor Fulfillment</h4>
                        
                    </div>
                </div>

            </div>

		)
	}
}

export default Wishlist
