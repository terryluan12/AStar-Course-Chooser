"use client";
import React, { useState, useEffect } from "react";
import Result from "./_components/Result";
import "@/css/Result.css";
import Label from "./_components/Label";
import "@/css/styles.css";
import { fetchWishlist, searchCourse } from "@/api.js";

function HomePage() {
  const [input, setInput] = useState("");
  const [results, setResults] = useState([]);
  const [wishlist, setWishlist] = useState([]);

  const handleChange = (event) => {
    setInput(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const res = await searchCourse(input);
    let results = [<Label key="empty"></Label>];
    switch (res.status) {
      case 200:
        if (res.data.length === 0) {
          alert("Course not found");
        } else {
          results.push(res.data.courses.map((result) => {
            let isStarred = false;
            if (wishlist.some((course) => course.course_code === result.course_code)) {
              isStarred = true;
            }
            return (
              <Result
                key={result.course_code}
                course_code={result.course_code}
                course_name={result.course_name}
                isStarred={isStarred}
              ></Result>
            )
          }
          ));
        }
        break;
      case 400:
        alert("400 Error. Please refresh");
        break;
      default:
        alert("Unknown Error. Please contact website owner");
        break;
    }

    setResults(results);
  };

  useEffect(() => {
    const username = localStorage.getItem("username")
    if (username) {
      fetchWishlist(username)
        .then((res) => {
          setWishlist(res.data.wishlist)
        })
    }
  }, [])


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

export default HomePage;
