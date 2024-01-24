import axios from 'axios';

const API_URL = 'http://localhost/api/';

class AuthService {
    login(user) {
        return axios
            .post(API_URL + 'token/', {
                username: user.username,
                password: user.password
            })
            .then(response => {
                if (response.data.access) {
                    localStorage.setItem('user', JSON.stringify(response.data));
                }
                return response.data;
            });
    }

    logout() {
        localStorage.removeItem('user');
    }

    refreshToken() {
        const user = JSON.parse(localStorage.getItem('user'));
        return axios
            .post(API_URL + 'token/refresh/', {
                refresh: user.refresh
            })
            .then(response => {
                if (response.data.access) {
                    user.access = response.data.access;
                    localStorage.setItem('user', JSON.stringify(user));
                }
                return response.data;
            });
    }
}

export default new AuthService();
