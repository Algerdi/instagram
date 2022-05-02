import axios from 'axios'
import {
  LOGIN_REQUEST,
  LOGIN_SUCCESS,
  LOGIN_FAILURE
} from './loginTypes'

export const login = () => {
  return (dispatch: any) => {
    dispatch(loginRequest())
    axios
      .get('https://jsonplaceholder.typicode.com/users')
      .then(response => {
        // response.data is the users
        const users = response.data
        dispatch(loginSuccess(users))
      })
      .catch(error => {
        // error.message is the error message
        dispatch(loginFailure(error.message))
      })
  }
}

export const loginRequest = () => {
  return {
    type: LOGIN_REQUEST
  }
}

export const loginSuccess = (users: any) => {
  return {
    type: LOGIN_SUCCESS,
    payload: users
  }
}

export const loginFailure = (error: any) => {
  return {
    type: LOGIN_FAILURE,
    payload: error
  }
}
