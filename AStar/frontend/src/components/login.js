import React, { Component, useState } from "react";
// import { propTypes } from "react-bootstrap/esm/Image";
import { render } from "react-dom";
// import { useHistory } from "react-router-dom";
import APIService from "./APIService";
import Wishlist from "./Wishlist";
import NavbarComp from "./Navbar";
// import Routes from "../routes";
import App from "../App";

// function Login (props) {
//   const [username, setUsername] = useState("");
//   const [password, setPassword] = useState("");
//   const history = useHistory();

//   const handleChange = (event) =>{
//     console.log("in handle change");
//     this.setState({
//       [event.target.name]: event.target.value
//     });
    
//   }

//   const handleLogin = (event) =>{
   
//           console.log("entered in handlelogin");
//           event.preventDefault();
//           // this.insertArticle(event); --> needs to be
//           // this.insertArticle(event)
//           // alert(
//           //   "you submitted: " +
//           //     username +
//           //     " and pass: " +
//           //     password
//           // );

//           // let data = this.username
//           this.props.setAccount(this.username)
//           history.push('/Wishlist')




//           // fetch('http://localhost:5000/login',{
//           //   method: 'POST',
//           //   headers:{ "Content-Type": "application/json"},
//           //   body: JSON.stringify({username:username, password: password})
//           // }).then((response)=>{
//           //   console.log("login details sent")
//           //   //if verified, redirect to mywishlist


//           // }).then((response)=>{
//           //     if(response.status_code == 200){

//           //       //login verified, go to wishlist with data ()
//           //       // history.push('/Wishlist')
//           //       alert("login verified")
//           //       return response;
//           //     }else if(response.status_code == 401){
//           //       alert("Incorrect Login Details. Try again.")
//           //       return response;
//           //     }
//           // }).catch( (error)=>{
//           //   console.log("Login error: " +error)
//           // })

//   }

//   return (
//     <div style={{ marginTop: "20%" }}>
//             <h1> Login</h1>
//             <form onSubmit={(e) =>handleLogin(e)}>
//               <input
//                 name="username"
//                 onChange={(e) =>setUsername(e.target.value)}
//                 required
//                 type="text"
//                 placeholder="Username"
//                 style={{ marginTop: "5%" }}
//               />
//               <br />
//               <input
//                 name="password"
//                 onChange={(e) =>setPassword(e.target.value)}
//                 required
//                 type="text"
//                 placeholder="Password"
//                 style={{ marginTop: "5%" }}
//               />
//               <br />
//               <button
//                 type="submit"
//                 className="myButton"
//                 style={{ marginTop: "5%" }}
//               >
//                 Login
//               </button>
//             </form>
    
//           </div>
//         );
//   }






class Login extends Component {
  // const [username, setUsername] = useState("");
  // const [password, setPassword] = useState("");

  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: ""
    };
    this.handleLogin = this.handleLogin.bind(this);
    this.handleChange = this.handleChange.bind(this);
    // this.setAccount=this.props.setAccount.bind(this);
    // this.history=useHistory()
  }

 

  // insertArticle(event) {
  //   APIService.insertArticle(this.state)
  //     .then((response) => event.insertedArticle(response))
  //     // should "event" be props?
  //     .catch((error) => console.log("error", error));
  // }

  handleChange(event) {
    console.log("in handle change");
    this.setState({
      [event.target.name]: event.target.value
    });
  }

  handleLogin(event) {
    console.log("entered here");
    event.preventDefault();
    // alert(
    //   "you submitted: " +
    //     this.state.username +
    //     " and pass: " +
    //     this.state.password
    // );

    // const userInfo = [{username: this.state.username, password: this.state.password}]
    // const userInfo = [this.state.username, this.state.password]
    this.props.setUsername(this.state.username);
    // this.props.setPassword(this.state.password);

    // this.props.history.push('/Wishlist');
   
  }
  render() {
    return (
      <div style={{ marginTop: "20%" }}>
        <h1> Login</h1>
        <form onSubmit={this.handleLogin}>
          <input
            name="username"
            onChange={this.handleChange}
            required
            type="text"
            placeholder="Username"
            style={{ marginTop: "5%" }}
          />
          <br />
          <input
            name="password"
            onChange={this.handleChange}
            required
            type="text"
            placeholder="Password"
            style={{ marginTop: "5%" }}
          />
          <br />
          <button
            type="submit"
            className="myButton"
            style={{ marginTop: "5%" }}
          >
            Login
          </button>
        </form>

      </div>
    );
  }
}


export default Login;