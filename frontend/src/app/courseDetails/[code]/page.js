import { CourseDescription } from "./_components/CourseDescription";
import { addWishlist, deleteWishlist } from "@/api.js";

function CourseDescriptionPage({ params }) {
  const toggleStar = async (isStarred) => {
    "use server";
    return isStarred
      ? deleteWishlist(params.code)
      : addWishlist(params.code);
  };

  return <CourseDescription toggleStar={toggleStar} />;
}

export default CourseDescriptionPage;
