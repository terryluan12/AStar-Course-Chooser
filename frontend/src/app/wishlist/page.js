"use client";
import React, { useState, useEffect } from "react";
import "../../css/wishlist.css";
import "bootstrap/dist/css/bootstrap.css";
import user_profile from "../../img/user.png";
import CourseCard from "./CourseCard";
import axios from "axios";
import MinorListCard from "./MinorListCard";
import Image from "next/image";

function Wishlist() {
  const [wishlist, setWishlist] = useState([]);
  const [minorlist, setMinorlist] = useState([]);
  const [username, setUsername] = useState(
    typeof window !== "undefined" ? localStorage.getItem("username") : null,
  );

  const fetchMinorData = async () => {
    return await axios.get(
      `${process.env.NEXT_PUBLIC_API_URL}/user/wishlist/minorCheck?username=${username}`,
      {
        username: username,
      },
    );
  };
  const fetchWishlistData = async () => {
    return await axios.get(
      `${process.env.NEXT_PUBLIC_API_URL}/user/wishlist?username=${username}`,
      {
        username: username,
      },
    );
  };

  useEffect(() => {
    setUsername(localStorage.getItem("username"));
    if (!username) {
      alert("ERROR: MUST BE LOGGED IN TO ACCESS WISHLIST");
    }
    const setWishlistPage = async () => {
      const res = await fetchWishlistData();

      if (res.status === 200) setWishlist(res.data.wishlist);
      else
        alert(
          "The system cannot return wishlist at the moment. Please try again later.",
        );
    };
    const checkMinor = async () => {
      const res = await fetchMinorData();
      let temp_minor_list = res.data.minorCheck.map((minor) => (
        <MinorListCard minor_name={minor.name} key={minor.name} />
      ));
      setMinorlist(temp_minor_list);
    };

    setWishlistPage().catch(console.error);
    // checkMinor().catch(console.error);
  }, []);

  return (
    <div className="wishlist-page-content">
      <div className="left-panel">
        <h1 className="wishlist-title">My Wishlist</h1>
        {!wishlist.length && (
          <h4 style={{ color: "#8198B8" }}>
            Search for courses and add them to your wishlist.
          </h4>
        )}
        <CourseCard
          className={"course-card-container"}
          wishlist_data={wishlist}
        ></CourseCard>
      </div>
      <div className="right-panel">
        <div className="centered">
          <Image layout="responsive" src={user_profile} alt="" />
          <h3>{username}</h3>
          <p>Computer Engineering Student</p>
          <br></br>
          <br></br>
          <h4>Minor Fulfillment</h4>
          <div className={"minor-display"}>{minorlist}</div>
        </div>
      </div>
    </div>
  );
}

export default Wishlist;
