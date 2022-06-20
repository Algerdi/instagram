import {
  LOGIN_REQUEST,
  LOGIN_SUCCESS,
  LOGIN_FAILURE
} from './loginTypes'

const initialState = {
  loading: false,
  user: {},
  error: ''
}

const loginReducer = (state = initialState, action: any) => {
  switch (action.type) {
    case LOGIN_REQUEST:
      return {
        ...state,
        loading: true
      }
    case LOGIN_SUCCESS:
      return {
        loading: false,
        users: action.payload,
        error: ''
      }
    case LOGIN_FAILURE:
      return {
        loading: false,
        users: {},
        error: action.payload
      }
    default: return state
  }
}

export default loginReducer
