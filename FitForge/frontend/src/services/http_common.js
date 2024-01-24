import axios from 'axios';
import AuthService from './auth_service';

const http = axios.create({
    baseURL: "http://localhost/api/",
    headers: {
        "Content-type": "application/json"
    }
});

http.interceptors.request.use(
    config => {
        const user = JSON.parse(localStorage.getItem('user'));
        if (user && user.access) {
            config.headers.Authorization = `Bearer ${user.access}`;
        }
        return config;
    },
    error => {
        Promise.reject(error);
    }
);

http.interceptors.response.use((response) => {
    return response;
}, function (error) {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
        originalRequest._retry = true;
        return AuthService.refreshToken().then(res => {
            if (res.access) {
                axios.defaults.headers.common['Authorization'] = 'Bearer ' + res.access;
                return axios(originalRequest);
            }
        });
    }
    return Promise.reject(error);
});

export default http;
