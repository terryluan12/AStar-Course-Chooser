"use client";
import React, { useState, useEffect, useContext } from "react";
import "@/css/wishlist.css";
import "bootstrap/dist/css/bootstrap.css";
import user_profile from "@/img/user.png";
import CourseCard from "./_components/CourseCard";
import Image from "next/image";
import { fetchWishlist } from "@/api.js";
import { UserContext } from "@/contexts";

function Wishlist() {
  const [wishlist, setWishlist] = useState([]);
  const [minorlist, _setMinorList] = useState([]);
  const { userContext, _setUserContext } = useContext(UserContext);

  useEffect(() => {
    if (!userContext.username) {
      alert("ERROR: MUST BE LOGGED IN TO ACCESS WISHLIST");
      return;
    }
    const setWishlistPage = async () => {
      fetchWishlist().then((res) => {
        if (res.status === 200) setWishlist(res.data.wishlist);
        else
          alert(
            "The system cannot return wishlist at the moment. Please try again later."
          );
      });
    };
    setWishlistPage().catch(console.error);
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
          wishlist_data={wishlist}></CourseCard>
      </div>
      <div className="right-panel">
        <div className="centered">
          <Image layout="responsive" src={user_profile} alt="" />
          <h3>{userContext.username}</h3>
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
