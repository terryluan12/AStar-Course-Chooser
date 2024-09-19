"use client";
import "@/css/Form.css";
import { useRouter } from "next/navigation";

export function Form({ children, onSubmit, name, redirect, button }) {
  // @todo add in JWT token usage
  const router = useRouter();
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
    );
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
