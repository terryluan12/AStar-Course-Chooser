import "@/css/Form.css";
import { cookies } from "next/headers";
// import { Form } from "./_components/Form";
import { loginAccount } from "@/api";
import { Form } from "@/app/_components/Form"

function LoginPage() {
  // @todo add in JWT token usage

  const handleLogin = async (username, password) => {
    "use server"

    return loginAccount(username, password).then(
      (res) => {
        cookies().set({
          name: "auth_token",
          value: res.data.token,
          httpOnly: true,
          path: "/",
        });
        return [res.data.message, res.data.status]
      }
    ).catch((err) => {
      const message = err.response.data.message ? err.response.data.message : "An unexpected error occurred"
      return [message, err.response.status]
    });
  };

  return (
    <Form name="Log In" onSubmit={handleLogin} />
  );
}

export default LoginPage;
