import NavbarComp from "./_components/Navbar";
import "@/css/global.css";

export const metadata = {
  title: "AStar Chooser",
  description:
    "A course finder allowing UofT Engineering students to choose courses",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>
        <div className="root">
          <div className="App">
            <NavbarComp />
            {children}
          </div>
        </div>
      </body>
    </html>
  );
}
