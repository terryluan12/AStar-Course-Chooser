import React, { Component } from "react";
import { Form, FormControl } from "react-bootstrap";
import "./css/coursecard.css";
import "bootstrap/dist/css/bootstrap.css";
// import wishlist_data from "../db/Wishlist_MOCK_data.json";

import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";
import ListGroupItem from "react-bootstrap/ListGroupItem";
// import CourseDescriptionPage from "./CourseDescription";


// this function should:
// receive  a list of courses called wishlist_data from the database
// send modified comments to database. database saves it. the page rerenders to show the modified information

class CourseCard extends Component{

  constructor(props){
    super(props)
    // this.courseCardDisplay=this.courseCardDisplay.bind(this)

  }

  render(){
     return (
    //  <div> {this.courseCardDisplay}</div>

    <div 
    >
      {console.log("wishlist data: ", this.props.wishlist_data)}
      {this.props.wishlist_data.map((course)=>(
        //go to course page when clicked
        <a href={`/course/details?code=${course.code}`}>
        <Card
        // className={"coursecard"}
        style={{
          width: "18rem",
          flex: 1,
          borderRadius: 30,
          // flexDirection: "row",
          padding: "10px"
        }}

        
      >
        {/* <Card.Img variant="top" src="holder.js/100px180?text=Image cap" /> */}
        <Card.Body>
          {/* <Card.Title>ECE444: Software Engineering</Card.Title> */}
          <Card.Title>
            {course.code}:{course.name} 
          </Card.Title>
          <ListGroup className="list-group-flush">
            <ListGroupItem>
              <div
                className="tags"
                style={{ border: "1px", background: "#FFF7CB" }}
              >
                {/* {course.Tags}{" "} */}
              </div>
            </ListGroupItem>
          </ListGroup>
          
        </Card.Body>
      </Card>
      </a>


      )



      )}
       
    </div>


    )
    
  }
}


// function CourseCard(props) {
//   // a diffrent way:
//   // https://stackoverflow.com/questions/53960988/how-do-i-make-my-react-bootstrap-cards-line-up-horizontally-and-equally-spaced
//   const courseCardDisplay = wishlist_data.map((course) => {
//     return (
//       //should go to course page when card is clicked
//       <Card
//         style={{
//           width: "18rem",
//           flex: 1,
//           borderRadius: 30,
//           // flexDirection: "row",
//           padding: "10px"
//         }}
//       >
//         {/* <Card.Img variant="top" src="holder.js/100px180?text=Image cap" /> */}
//         <Card.Body>
//           {/* <Card.Title>ECE444: Software Engineering</Card.Title> */}
//           <Card.Title>
//             {course.Course_Code}:{course.Name}
//           </Card.Title>
//           <ListGroup className="list-group-flush">
//             <ListGroupItem>
//               <div
//                 className="tags"
//                 style={{ border: "1px", background: "#FFF7CB" }}
//               >
//                 {course.Tags}{" "}
//               </div>
//             </ListGroupItem>
//           </ListGroup>
//           <div className="card-subtext">
//             <Card.Text>
//               <b>My Notes</b>
//               <br />
//               {course.Notes}
//             </Card.Text>
//           </div>
//         </Card.Body>

//         <Card.Body style={{height: "50%"}}>
//           {/* <Card.Link href="#">Card Link</Card.Link>
//             <Card.Link href="#">Another Link</Card.Link> */}
//             {/* <input
//             type="text"
//             value={course.Notes}
//             // onChange={this.handleChange}
//          /> */}
//           <Form
//             style={{
//               display: "flex"
//             }}
//           >
//             <FormControl
//               type="text"
//               placeholder="Comments"
//               className="mr-sm-2"
//               style={{ width: "100%", height: "50%"}}
//               // onChange={handleChange}
//             />
//             {/* should send query word, search database, return list of items and display results when search button is clicked */}
//           </Form>
//         </Card.Body>
//       </Card>
//     );
//   });

//   return <div> {courseCardDisplay}</div>;
// }

export default CourseCard;
