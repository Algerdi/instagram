import axios from 'axios';

const baseURL = 'http://localhost:8000/';

const api = axios.create({
  baseURL: baseURL,
  timeout: 5000,
  headers: {
    Authorization: (localStorage.getItem('access_token')
      ? 'JWT ' + localStorage.getItem('access_token')
      : ""),
    'Content-Type': 'application/json',
    accept: 'application/json',
  },
});
api.interceptors.response.use(
  response => response,
  error => {
    const originalRequest = error.config;
    if (error.response.status === 401 && error.response.statusText === "Unauthorized") {
      const refresh_token = localStorage.getItem('refresh_token');
      return api
        .post('/token/refresh/', {refresh: refresh_token})
        .then((response) => {

          localStorage.setItem('access_token', response.data.access);
          localStorage.setItem('refresh_token', response.data.refresh);
          (api.defaults.headers as any)['Authorization'] = "JWT " + response.data.access;
          originalRequest.headers['Authorization'] = "JWT " + response.data.access;

          return api(originalRequest);
        })
        .catch(err => {
          console.log(err)
        });
    }
    return Promise.reject(error);
  }
);

export default api;
