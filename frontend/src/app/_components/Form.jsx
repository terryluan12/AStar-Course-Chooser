"use client";
import "@/css/Form.css";
import { useRouter } from "next/navigation";
import { useContext } from "react";
import { UserContext } from "@/contexts";

export function Form({ children, onSubmit, name, redirect, button, doLogin }) {
  // @todo check if there's a better way to implement isLogin
  const router = useRouter();
  const { _, setUserContext } = useContext(UserContext);

  const handler = async (event) => {
    event.preventDefault();
    const names = children.map((child) => {
      if (child.type !== "input") {
        throw new Error("Form children must be input elements");
      }
      return child.props.name;
    });

    const [message, status_code] = await onSubmit(
      ...names.map((name) => event.target[name].value)
    ).then((res) => {
      if (doLogin) {
        setUserContext({
          loggedIn: true,
          username: event.target.username.value,
        });
      }
      return res;
    });
    alert(message);
    if (status_code === 200 && redirect) {
      router.push(redirect);
    }
  };

  return (
    <form onSubmit={handler} className={"astar-form"}>
      <h1>{name}</h1>
      {children}
      <button type="submit">{button ? button : name}</button>
    </form>
  );
}

export default Form;
