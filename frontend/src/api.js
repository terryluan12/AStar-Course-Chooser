"use server"
import axios from 'axios'
import { cookies } from 'next/headers'

axios.interceptors.request.use(function (config) {
    // @todo figure out why this is necessary, instead of setting in request (fetchWishlist is an issue here)
    config.headers.Cookie = `session_token=${cookies().get("session_token").value}`
    return config;
}, function (error) {
    return Promise.reject(error);
});

// =============================Course Functionalities=============================

export async function searchCourse(course_code) {
    return axios.get(
        `${process.env.NEXT_PUBLIC_API_URL}/course/search?course_code=${course_code}`,
    );
};

export async function fetchCourse(course_code) {
    return axios.get(
        `${process.env.NEXT_PUBLIC_API_URL}/course?course_code=${course_code}`,
    ).then((res) => {
        return { "data": res.data, "status": res.status };
    });
}

// =============================User Functionalities=============================

export async function loginAccount(username, password) {
    return axios.post(`${process.env.NEXT_PUBLIC_API_URL}/session`, {
        username: username,
        password: password,
    });
}
export async function logoutAccount() {
    return axios.delete(`${process.env.NEXT_PUBLIC_API_URL}/session`);
}

export async function signupAccount(username, password) {
    return axios.post(`${process.env.NEXT_PUBLIC_API_URL}/user`, {
        username: username,
        password: password,
    });
}

// =============================Wishlist Functionalities=============================

export async function fetchWishlist() {
    return axios.get(`${process.env.NEXT_PUBLIC_API_URL}/wishlist`
    ).then((res) => {
        return { "data": res.data, "status": res.status };
    });
}

export async function addWishlist(course_code) {
    return axios.post(
        `${process.env.NEXT_PUBLIC_API_URL}/wishlist?course_code=${course_code}`
    ).then((res) => {
        return { "data": res.data, "status": res.status };
    });
}
export async function deleteWishlist(course_code) {
    return axios.delete(
        `${process.env.NEXT_PUBLIC_API_URL}/wishlist?course_code=${course_code}`
    ).then((res) => {
        return { "data": { "message": res.data.message }, "status": res.status };
    });
}

// =============================Minor Functionalities=============================

export async function fetchMinor(username) {
    return axios.get(
        `${process.env.NEXT_PUBLIC_API_URL}/wishlist/minorCheck?username=${username}`,
        {
            username: username,
        },
    );
}