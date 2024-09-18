"use client";

import React, { useState, useEffect } from "react";
import Image from "next/image";
import "@/css/course-description.css";
import "bootstrap/dist/css/bootstrap.css";
import Container from "react-bootstrap/Container";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
// import requisite_label from "../../../img/requisite-label.png";
import empty_star from "@/img/star.png";
import starred_star from "@/img/starred.png";
import { addWishlist, deleteWishlist, fetchWishlist, fetchCourse } from "@/api.js";

function CourseDescriptionPage(props) {
  let star = empty_star;

  const [course, setCourse] = useState({
    course_code: props.params.code,
    course_name: "",
    division: "Faculty of Applied Science and Engineering",
    department:
      "Department of Edward S. Rogers Sr. Dept. of Electrical & Computer Engineering",
    graph: "",
    course_description: "",
    syllabus: "",
    prerequisites: "",
    corequisites: "",
    exclusions: "",
    starred: false,
    graphics: [],
    username: null
  });


  const toggleStar = async () => {
    if (!course.starred) {
      return await addWishlist(course.username, course.course_code);
    } else {
      return await deleteWishlist(course.username, course.course_code);
    }
  };

  useEffect(() => {
    const setCoursePage = async () => {
      const course_res = await fetchCourse(course.course_code).then((res) => res.data.course);
      const username = localStorage.getItem("username")
      let isStarred = false
      if (username) {
        const wishlist = await fetchWishlist(username).then((res) => res.data.wishlist);
        isStarred = wishlist.some(
          (wishlist_course) => wishlist_course.course_code === course.course_code,
        );
      }

      const syllabus_link =
        "http://courses.skule.ca/course/" + course.course_code;

      //temp_graph.push(<ShowGraph graph_src={graph}></ShowGraph>)
      setCourse({
        ...course,
        course_name: course_res.course_name,
        graph: course_res.graph,
        course_description: course_res.description,
        syllabus: syllabus_link,
        prerequisites: course_res.prerequisite,
        corequisites: course_res.corequisite,
        exclusions: course_res.exclusion,
        graphics: null,
        username: username,
        starred: isStarred
      });
    };

    setCoursePage().catch(console.error);
  }, []);

  const check_star = async () => {
    if (course.username) {
      const res = await toggleStar();
      setCourse({ ...course, starred: !course.starred });
      star = star == empty_star ? starred_star : empty_star;
      if (res.status != 200) {
        alert("error occured while modifying wishlist: ", res.status);
      }
    } else {
      //else, notify
      alert("You must login to save a course.");
    }
  };

  const openLink = () => {
    const newWindow = window.open(
      course.syllabus,
      "_blank",
      "noopener,noreferrer",
    );
    if (newWindow) {
      newWindow.opener = null;
    }
  };

  return (
    <div className="page-content">
      <Container className="course-template">
        <Row float="center" className="course-title">
          <Col xs={8}>
            <h1>
              {course.course_code} : {course.course_name}
            </h1>
          </Col>
          <Col xs={4}>
            <Image
              src={course.starred ? starred_star : empty_star}
              onClick={check_star}
              alt=""
            />
          </Col>
        </Row>
        <Row>
          <Col className="col-item">
            <h3>Division</h3>
            <p>{course.division}</p>
          </Col>
          <Col className="col-item">
            <h3>Department</h3>
            <p>{course.department}</p>
          </Col>
          <Col className="col-item">
            <h3>Past Tests and Syllabi</h3>
            <button className={"syllabus-link"} onClick={openLink}>
              View
            </button>
          </Col>
        </Row>
        <Row className="col-item course-description">
          <h3>Course Description</h3>
          <p>{course.course_description}</p>
        </Row>
        <Row className="col-item course-requisite">
          <Row>
            <h3>Course Requisites</h3>
          </Row>
          <Row>
            <Col className="requisites-display">
              <h4>Pre-Requisites</h4>
              <p>{course.prerequisites}</p>
            </Col>
            <Col className="requisites-display">
              <h4>Co-Requisites</h4>
              <p>{course.corequisites}</p>
            </Col>
            <Col className="requisites-display">
              <h4>Exclusion</h4>
              <p>{course.exclusions}</p>
            </Col>
          </Row>
          <Row>
            {/* <div className={"req-graph"}>
              <img style={{ width: "70%", marginBottom: "3%" }} alt="" src={requisite_label} />
              <img src={`data:image/jpeg;base64,${course.graph}`} alt="" />
            </div> */}
          </Row>
        </Row>
      </Container>
    </div>
  );
}

export default CourseDescriptionPage
