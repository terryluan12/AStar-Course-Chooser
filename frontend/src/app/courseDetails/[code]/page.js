import { CourseDescription } from "./_components/CourseDescription";
import { addWishlist, deleteWishlist } from "@/api.js";

function CourseDescriptionPage() {
  const toggleStar = async (course) => {
    "use server"
    return course.isStarred ? deleteWishlist(course.course_code) : addWishlist(course.course_code);
  };

  return (
    <CourseDescription toggleStar={toggleStar} />
  );
}

export default CourseDescriptionPage
