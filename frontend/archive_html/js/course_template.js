var wishlist = [];

function starred(){
    document.getElementById('star').src = "img/starred.png"
    var course_name = document.getElementById('course-title').textContent;
    console.log(course_name);
    wishlist.push(course_name);
    console.log(wishlist[0]);
}

// pass in search result 
function get_syllabus(course="https://shuiblue.github.io/UofT-ECE444/") {
    window.open(course);
}