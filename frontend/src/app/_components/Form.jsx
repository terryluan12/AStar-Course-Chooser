"use client";
import "@/css/Form.css";
import { useRouter } from "next/navigation";

export function Form({ onSubmit, name }) {
  // @todo add in JWT token usage
  const router = useRouter();
  const handler = async (event) => {
    event.preventDefault();
    const [message, status_code] = await onSubmit(
      event.target.username.value,
      event.target.password.value
    );
    alert(message);
    if (status_code === 200) {
      router.push("/wishlist");
    }
  };

  return (
    <div className={"sign-up"}>
      <h1>{name}</h1>
      <form onSubmit={handler}>
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
          {name}
        </button>
      </form>
    </div>
  );
}

export default Form;
