import { logoutAccount } from "@/api";
import { cookies } from "next/headers";
import NavbarComp from "./_components/Navbar";
import { UserContextProvider } from "@/contexts";
import "@/css/global.css";

export const metadata = {
  title: "AStar Chooser",
  description:
    "A course finder allowing UofT Engineering students to choose courses"
};

export default function RootLayout({ children }) {
  const logoutFunction = async () => {
    "use server";
    return logoutAccount().then((_) => {
      cookies().remove("session_token");
    });
  };
  const getInitialContext = async () => {
    "use server";
    // @todo make an endpoint to check if session token is valid
    const isValid = cookies().get("session_token").value !== null;
    return { loggedIn: isValid, username: isValid ? "username" : null };
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
