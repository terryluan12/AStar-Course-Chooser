import { logoutAccount } from "@/api";
import { cookies } from "next/headers";
import NavbarComp from "./_components/Navbar";
import { UserContextProvider } from "@/contexts";
import "@/css/global.css";

// @todo separate base components to a _components folder and a global components folder
export const metadata = {
  title: "AStar Chooser",
  description:
    "A course finder allowing UofT Engineering students to choose courses"
};

export default function RootLayout({ children }) {
  const logoutFunction = async () => {
    "use server";
    return logoutAccount().then((_) => {
      cookies().delete("session_token");
    });
  };
  const getInitialContext = async () => {
    "use server";
    // @todo make an endpoint to check if session token is valid
    const isLoggedIn = cookies().has("session_token");
    return { loggedIn: isLoggedIn, username: isLoggedIn ? "username" : null };
  };

  return (
    <html lang="en">
      <body>
        <div className="root">
          <div className="App">
            <UserContextProvider>
              <NavbarComp
                logoutFunction={logoutFunction}
                getInitialContext={getInitialContext}
              />
              {children}
            </UserContextProvider>
          </div>
        </div>
      </body>
    </html>
  );
}
