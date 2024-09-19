"use client";
import { useRouter } from "next/navigation";
import "@/css/Form.css";
import { loginAccount } from "@/api.js";

function LoginPage() {
  // @todo add in JWT token usage
  const router = useRouter();

  const handleLogin = async (event) => {
    event.preventDefault();
    const formData = {
      username: event.target.username.value,
      password: event.target.password.value
    }

    const res = await loginAccount(formData.username, formData.password).then(
      (res) => {
        localStorage.setItem("username", formData.username);
        router.refresh();
        router.push("/wishlist");
        return res
      }
    ).catch((err) => {
      return err.response
    });
    alert(res.data.message)
  };

  return (
    <div className={"sign-up"}>
      <h1>Log In</h1>
      <form onSubmit={handleLogin}>
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
          Log In
        </button>
      </form>
    </div>
  );
}

export default LoginPage;
