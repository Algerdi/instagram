import axios from "axios";
import api from "../../axios/axios";
import {
  LOGIN_REQUEST,
  LOGIN_SUCCESS,
  LOGIN_FAILURE
} from './loginTypes';

export const login = (email: string, password: string) => {
  return (dispatch: any) => {
    dispatch(loginRequest())
    axios.post("http://localhost:8000/api/token/", {
      email: email,
      password: password
    })
      .then(response => {
        if (response.status === 200) {
          (api.defaults.headers as any)['Authorization'] = "JWT " + response.data.access;
          localStorage.setItem('access_token', response.data.access);
          localStorage.setItem('refresh_token', response.data.refresh);
          console.log(response.data.access);
          console.log(response.data.refresh);
          dispatch(loginSuccess([
            response.data.refresh,
            response.data.access
          ]))
        } else {
          dispatch(loginFailure(response))
        }
      })
      .catch(error => {
        dispatch(loginFailure(error.response))
      });
  }
}

export const loginRequest = () => {
  return {
    type: LOGIN_REQUEST
  }
}

export const loginSuccess = (tokens: any) => {
  return {
    type: LOGIN_SUCCESS,
    payload: tokens
  }
}

export const loginFailure = (error: any) => {
  return {
    type: LOGIN_FAILURE,
    payload: error
  }
}
