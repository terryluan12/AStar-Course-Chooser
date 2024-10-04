"use client";
import { useRouter } from "next/navigation";
import { useContext, useEffect } from "react";
import "@/css/navbar.css";
import "bootstrap/dist/css/bootstrap.css";
import logo from "@/img/logo.png";
import { Navbar, Nav } from "react-bootstrap";
import Link from "next/link";
import Image from "next/image";
import { UserContext } from "@/contexts";

let userInitialized = false;

function NavbarComp({ logoutFunction, username }) {
  const router = useRouter();
  const { userContext, setUserContext } = useContext(UserContext);
  useEffect(() => {
    if (!userInitialized) {
      userInitialized = true;
      setUserContext({ username: username });
    }

  }, []);

  const logOut = () => {
    logoutFunction();
    setUserContext({ username: null });
    router.push("/");
    router.refresh();
  };

  return (
    <div>
      <Navbar bg="myBlue" variant="dark" sticky="top" expand="lg">
        <Navbar.Brand>
          <Image style={{ width: "100%", height: "auto" }} src={logo} alt="" />{" "}
          <Nav.Link href="/" as={Link} style={{ color: "white", display: "inline" }}>
            A* Course Finder
          </Nav.Link>
        </Navbar.Brand>

        <Navbar.Toggle />
        <Navbar.Collapse>
          <Nav>
            <Nav.Link as={Link} href="/">
              Search
            </Nav.Link>

            {userContext.username && (
              <Nav.Link as={Link} href="/wishlist">
                My Wishlist
              </Nav.Link>
            )}

            {!userContext.username ? (
              <Nav.Link as={Link} href="/login">
                Login
              </Nav.Link>
            ) : (
              <Nav.Link onClick={logOut} as={Link} href="/">
                Logout
              </Nav.Link>
            )}

            {!userContext.username && (
              <Nav.Link as={Link} href="/signup">
                Sign Up
              </Nav.Link>
            )}
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    </div>
  );
}

export default NavbarComp;
