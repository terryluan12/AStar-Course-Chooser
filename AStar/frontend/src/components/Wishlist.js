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

class Wishlist extends Component {

	render() {
		return(

            <div className="wishlist-page-content">
                 <div className="left-panel">
          <Container>
            <h1 className="wishlist-title">My Wishlist</h1>

            <CourseCard style={{ display: "flex", flexDirection: "row" }} />
            {/* {CourseCard} */}
          </Container>
        </div>
                <div className="right-panel">
                    <div className="centered">
                        <img src={user_profile}></img>
                        <h3>John Doe</h3>
                        <p>Computer Engineering Student</p>
                        <br></br>
                        <br></br>
                        <h4>Minor/Certificate Progress</h4>
                        <img src={minor_label} width="100%"></img>
                        <Dropdown>
                            <Dropdown.Toggle variant="success" id="dropdown-basic" className="add-button">
                            + Add Minor/Certificate
                            </Dropdown.Toggle>

                            <Dropdown.Menu>
                                <Dropdown.Item href="#/action-1">Artificial Intelligence Minor</Dropdown.Item>
                                <Dropdown.Item href="#/action-2">Engineering Business Minor</Dropdown.Item>
                                <Dropdown.Item href="#/action-3">Biomedical Engineering Minor</Dropdown.Item>
                            </Dropdown.Menu>
                        </Dropdown>
                    </div>
                </div>

            </div>

		)
	}
}

export default Wishlist
