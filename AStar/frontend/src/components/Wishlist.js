import React, { Component } from 'react';
import './css/wishlist.css';
import 'bootstrap/dist/css/bootstrap.css';
import user_profile from './img/user.png'
import CourseCard from "./CourseCard";
import axios from "axios"
import MinorListCard from './MinorListCard'

class Wishlist extends Component {

    constructor(props){
        super(props)
        this.state={
            wishlist_data:[],
            minor_list: [],
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

        axios.get(`http://localhost:5000/user/wishlist/minorCheck?username=${this.state.username}`, {
            'username': this.state.username
        })
        .then(res => {
            console.log("res: ", res.data.minorCheck)
            let len = res.data.minorCheck.length
            let temp_minor_list = []
            for (let i = 0; i < len; i++) {
                temp_minor_list.push(<MinorListCard minor_name={res.data.minorCheck[i].name}></MinorListCard>)
            }

            this.setState({minor_list: temp_minor_list})
           
        })      
    }

    
	render() {
		return(

            <div className="wishlist-page-content">
                <div className="left-panel">
                <h1 className="wishlist-title">My Wishlist</h1>    
                {!this.state.wishlist_data.length && <h4 style={{color: '#8198B8'}}>Search for courses and add them to your wishlist.</h4>}      
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
                        <div className={"minor-display"}>
                            {this.state.minor_list}
                        </div>
                        
                    </div>
                </div>

            </div>

		)
	}
}

export default Wishlist
