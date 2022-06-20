import api from "../../axios/axios";
import {
  REGISTER_REQUEST,
  REGISTER_SUCCESS,
  REGISTER_FAILURE
} from './registerTypes';

export const register = (email: string, username: string, name: string, password: string) => {
  return (dispatch: any) => {
    dispatch(registerRequest())
    api.post("users/register", {
      email: email,
      user_name: username,
      name: name,
      password: password,
    })
      .then(response => {
        if (response.status === 201) {
          alert("User successfully registered")
          console.log(response.data)
          dispatch(registerSuccess([
            response.data
          ]))
        } else {
          dispatch(registerFailure(response))
        }
      })
      .catch(error => {
        dispatch(registerFailure(error.response))
      });
  }
}

export const registerRequest = () => {
  return {
    type: REGISTER_REQUEST
  }
}

export const registerSuccess = (user: any) => {
  return {
    type: REGISTER_SUCCESS,
    payload: user
  }
}

export const registerFailure = (error: any) => {
  return {
    type: REGISTER_FAILURE,
    payload: error
  }
}
