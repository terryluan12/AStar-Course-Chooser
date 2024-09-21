import Result from "./_components/Result";
import Search from "./_components/Search";
import "@/css/Result.css";
import Label from "./_components/Label";
import "@/css/styles.css";
import { fetchWishlist, searchCourse } from "@/api.js";

function HomePage() {
  // @todo fix hydration error

  const handleSubmit = async (input, isLoggedIn) => {
    "use server"
    let wishlist = [];
    if (isLoggedIn) {
      wishlist = (await fetchWishlist()).data.wishlist
    };

    return searchCourse(input).then((res) => {
      let results = [<Label key="empty"></Label>];
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
      return results;
    }).catch((err) => {
      return [[], err.response.status];
    });
  }


  return (
    <Search handler={handleSubmit} />
  );
}

export default HomePage;
