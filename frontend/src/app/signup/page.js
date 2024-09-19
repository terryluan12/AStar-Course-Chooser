'use client';
import { useRouter } from "next/navigation";
import { signupAccount } from "@/api.js";
import "@/css/Form.css";

function SignupPage() {
  // @todo: look into using server actions
  // @todo: look into using direct form "action" submission
  const router = useRouter();

  const handleSignup = async (event) => {
    event.preventDefault();
    const formData = {
      username: event.target.username.value,
      password: event.target.password.value
    }

    const res = await signupAccount(formData.username, formData.password).then((res) => {
      localStorage.setItem("username", formData.username);
      router.push("/wishlist");
    }).catch((err) => {
      return err.response
    });
    alert(res.data.message)
  };

  return (
    <div className={"sign-up"}>
      <h1>Sign Up</h1>
      <form onSubmit={handleSignup}>
        <input
          name="username"
          required
          type="text"
          placeholder="Username"
          className={"signup-input"}
        />
        <br />
        <input
          name="password"
          required
          type="password"
          placeholder="Password"
          className={"signup-input"}
        />
        <br />
        <button type="submit" className="signup-button">
          Sign Up
        </button>
      </form>
    </div >
  );
}

export default SignupPage;
