import React, { Component } from "react";
import { useHistory, useState } from "react-router-dom";

// export default class Login extends Component {
//   render() {
//     return (
//       <div>
//         <h1> Login</h1>
//       </div>
//     );
//   }
// }

function Login(props) {
  // const username = useFormInput('');
  // const password = useFormInput('');
  // const [error, setError] = useState(null);
  // const [loading, setLoading] = useState(false);

  return (
    <div style={{ marginTop: "20%" }}>
      <h1> Login</h1>
      <input type="text" placeholder="Username" style={{ marginTop: "5%" }} />
      <br />
      <input type="text" placeholder="Password" style={{ marginTop: "5%" }} />
      <br />
      <button
        className="myButton"
        style={{ marginTop: "5%" }}
      >
        Login
      </button>
    </div>
  );
}

export default Login;
