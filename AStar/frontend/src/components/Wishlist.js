import React, { Component } from 'react';
import './css/wishlist.css';
import 'bootstrap/dist/css/bootstrap.css';
import user_profile from './img/user.png'
import CourseCard from "./CourseCard";
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

        this.setState({username: localStorage.getItem('username')})

        axios.get(`http://localhost:5000/user/wishlist?username=${this.state.username}`, {
            'username': this.state.username
        })
        .then(res => {
            if(res.status === 200){
                this.setState({wishlist_data: res.data.wishlist.course})
            }
            else {
                alert("The system cannot return wishlist at the moment. Please try again later.")
            }
        })      
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
