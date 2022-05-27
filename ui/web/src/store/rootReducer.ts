import { combineReducers } from 'redux'
import loginReducer from './login/loginReducer'
import registerReducer from "./register/registerReducer";

const rootReducer = combineReducers({
  login: loginReducer,
  register: registerReducer,
})

export default rootReducer
