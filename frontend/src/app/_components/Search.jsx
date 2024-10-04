"use client";
import React, { useState, useContext } from "react";
import { UserContext } from "@/contexts";
import "@/css/Result.css";
import "@/css/styles.css";

function Search({ handler }) {
  const { userContext, _ } = useContext(UserContext);
  const [input, setInput] = useState("");
  const [results, setResults] = useState([]);

  const handleChange = (event) => {
    setInput(event.target.value);
  };
  const handleSubmit = async (event) => {
    event.preventDefault();
    const res = await handler(input, userContext.username);
    setResults(res);
  };

  return (
    <div className="SearchQuery">
      <div style={{ marginTop: "10%" }}>
        <h1> A* Course Finder Search</h1>
        <form onSubmit={handleSubmit} className={"search"}>
          <input
            placeholder={"Search for course code, course name, keyword ..."}
            className={"text-input"}
            type="text"
            value={input}
            onChange={handleChange}
          />
          <input type="submit" value="Submit" className={"submit-button"} />
        </form>
      </div>

      <div className={"search-result-display"}>{results}</div>
    </div>
  );
}

export default Search;
