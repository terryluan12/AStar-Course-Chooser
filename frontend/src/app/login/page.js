import { cookies } from "next/headers";
import { loginAccount } from "@/api";
import { Form } from "@/app/_components/Form";

function LoginPage() {
  // @todo add in JWT token usage

  const handleLogin = async (username, password) => {
    "use server";

    return loginAccount(username, password)
      .then((res) => {
        cookies().set({
          name: "session_token",
          value: res.data.token,
          httpOnly: true,
          path: "/",
          domain: "localhost"
        });
        return [res.data.message, res.status];
      })
      .catch((err) => {
        const message = err.response.data.message
          ? err.response.data.message
          : "An unexpected error occurred";
        return [message, err.response.status];
      });
  };

  return (
    <Form
      name="Log In"
      onSubmit={handleLogin}
      redirect="/wishlist"
      doLogin={true}>
      <input name="username" required type="text" placeholder="Username" />
      <input name="password" required type="password" placeholder="Password" />
    </Form>
  );
}

export default LoginPage;
