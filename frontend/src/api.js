import axios from 'axios'


// =============================Course Functionalities=============================

export async function searchCourse(code) {
    return axios.get(
        `${process.env.NEXT_PUBLIC_API_URL}/course/search?course_code=${code}`,
    );
};

export async function fetchCourse(course_code) {
    return axios.get(
        `${process.env.NEXT_PUBLIC_API_URL}/course?course_code=${course_code}`,
    );
}

// =============================User Functionalities=============================

export async function loginAccount(username, password) {
    return await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/session`, {
        username: username,
        password: password,
    });
}

export async function signupAccount(username, password) {
    return await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/user`, {
        username: username,
        password: password,
    });
}

// =============================Wishlist Functionalities=============================

export async function fetchWishlist(username) {
    return axios.get(`${process.env.NEXT_PUBLIC_API_URL}/wishlist?username=${username}`)
}

export async function addWishlist(username, course_code) {
    return axios.post(
        `${process.env.NEXT_PUBLIC_API_URL}/wishlist?username=${username}&course_code=${course_code}`,
        {
            username: username,
            course_code: course_code,
        },
    );
}
export async function deleteWishlist(username, course_code) {
    return axios.delete(
        `${process.env.NEXT_PUBLIC_API_URL}/wishlist?username=${username}&course_code=${course_code}`,
        {
            course_code: course_code,
            username: username,
        },
    );
}

// =============================Minor Functionalities=============================

export async function fetchMinor(username) {
    return await axios.get(
        `${process.env.NEXT_PUBLIC_API_URL}/wishlist/minorCheck?username=${username}`,
        {
            username: username,
        },
    );
}