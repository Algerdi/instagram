import {
  REGISTER_REQUEST,
  REGISTER_SUCCESS,
  REGISTER_FAILURE
} from './registerTypes'

const initialState = {
  loading: false,
  user: {},
  error: ''
}

const registerReducer = (state = initialState, action: any) => {
  switch (action.type) {
    case REGISTER_REQUEST:
      return {
        ...state,
        loading: true
      }
    case REGISTER_SUCCESS:
      return {
        loading: false,
        user: action.payload,
        error: ''
      }
    case REGISTER_FAILURE:
      return {
        loading: false,
        user: {},
        error: action.payload
      }
    default: return state
  }
}

export default registerReducer
