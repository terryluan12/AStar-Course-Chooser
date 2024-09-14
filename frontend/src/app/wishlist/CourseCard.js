import React from "react";
import "../../css/coursecard.css";
import "bootstrap/dist/css/bootstrap.css";
import Col from "react-bootstrap/Col";
import Link from "next/link";

// this function should:
// receive  a list of courses called wishlist_data from the database
// send modified comments to database. database saves it. the page rerenders to show the modified information

function CourseCard(props) {
  return (
    <div className={"course-card-render"}>
      {props.wishlist_data.map((course) => (
        <Link
          href={`/courseDetails/${course.code}`}
          className={"wishlist-link"}
        >
          <Col className={"text-center wishlist-card"}>
            <h5>
              {course.code}: {course.name}
            </h5>
          </Col>
        </Link>
      ))}
    </div>
  );
}

export default CourseCard;
