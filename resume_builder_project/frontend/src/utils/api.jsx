// frontend/src/utils/api.js
import getCookie from './csrf.jsx'; // Add .jsx extension
import axios from 'axios';

const csrftoken = getCookie('csrftoken');

const api = axios.create({
    baseURL: '/api/',
    withCredentials: true,
});

if (csrftoken) {
    api.defaults.headers.common['X-CSRFToken'] = csrftoken;
}

api.defaults.headers.post['Content-Type'] = 'application/json';

export default api;