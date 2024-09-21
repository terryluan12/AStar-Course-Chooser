import { cookies } from "next/headers";
import { signupAccount, loginAccount } from "@/api.js";
import { Form } from "@/app/_components/Form";

function SignupPage() {

  const handleSignup = async (username, password) => {
    "use server"

    return signupAccount(username, password).then(() => {
      return loginAccount(username, password).then((res) => {
        cookies().set({
          name: "session_token",
          value: res.data.token,
          httpOnly: true,
          path: "/",
        });
        return [res.data.message, res.status]
      })
    }).catch((err) => {
      const message = err.response.data.message ? err.response.data.message : "An unexpected error occurred"
      return [message, err.response.status]
    });
  };

  return (
    <Form name="Sign Up" onSubmit={handleSignup} redirect="/wishlist" doLogin={true} >
      <input
        name="username"
        required
        type="text"
        placeholder="Username"
      />
      <input
        name="password"
        required
        type="password"
        placeholder="Password"
      />
    </Form>

  );
}

export default SignupPage;
