"use client";

import React, { useState, useEffect, useContext } from "react";
import Image from "next/image";
import "@/css/course-description.css";
import "bootstrap/dist/css/bootstrap.css";
import Container from "react-bootstrap/Container";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import { fetchWishlist, fetchCourse } from "@/api.js";
// import requisite_label from "../../../img/requisite-label.png";
import empty_star from "@/img/star.png";
import starred_star from "@/img/starred.png";
import { useParams } from "next/navigation";
import { UserContext } from "@/contexts";

export const CourseDescription = ({ toggleStar }) => {
  const { userContext, _ } = useContext(UserContext);

  const params = useParams();

  const [course, setCourse] = useState({
    course_code: params.code,
    course_name: "",
    division: "Faculty of Applied Science and Engineering",
    department:
      "Department of Edward S. Rogers Sr. Dept. of Electrical & Computer Engineering",
    course_description: "",
    syllabus: "",
    prerequisites: "",
    corequisites: "",
    exclusions: "",
    isStarred: false,
  });

  const check_star = async () => {
    if (userContext.loggedIn) {
      toggleStar(course).then((res) => {
        if (res.status != 200) {
          alert("error occured while modifying wishlist: ", res.status);
        } else {
          setCourse({ ...course, isStarred: !course.isStarred });
        }
      });
    } else {
      alert("You must login to save a course.");
    }
  };
  useEffect(() => {
    fetchCourse(params.code).then((course_res) => {
      const fetched_course = course_res.data.course;
      const syllabus_link =
        "http://courses.skule.ca/course/" + course.course_code;
      setCourse({
        ...course,
        course_name: fetched_course.course_name,
        course_description: fetched_course.description,
        syllabus: syllabus_link,
        prerequisites: fetched_course.prerequisite,
        corequisites: fetched_course.corequisite,
        exclusions: fetched_course.exclusion,
      });
    });
  }, []);
  useEffect(() => {
    let isStarred = false;
    fetchWishlist().then((res) => {
      if (userContext.loggedIn) {
        isStarred = res.data.wishlist.some((wishlist_course) => {
          return wishlist_course.course_code === course.course_code;
        });
        setCourse({ ...course, isStarred: isStarred });
      }
    });
  }, [userContext.loggedIn]);

  const openLink = () => {
    const newWindow = window.open(
      course.syllabus,
      "_blank",
      "noopener,noreferrer"
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
              src={course.isStarred ? starred_star : empty_star}
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
};
