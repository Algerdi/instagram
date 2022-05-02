import React, { useEffect } from 'react'
import { connect } from 'react-redux'
import { login } from '../redux/login/loginActions'
import "../styles/login/login.css"
import background from "../styles/login/images/phone-frame.png"

// @ts-ignore
function Login ({ userData, login }) {
  useEffect(() => {
    login()
  }, [])
  console.log(userData)
  return userData.loading ? (
    <h2>Loading</h2>
  ) : userData.error ? (
    <h2>{userData.error}</h2>
  ) : (
    <>
      <div className="container">
        <div className="main-container">
          <div className="main-content">
            <div className="slide-container" style={{ backgroundImage: `url(${background})` }}>
              <div className="slide-content" id="slide-content">
                <img src={require("../styles/login/images/slide (1).jpg")} alt="slide image" className="active" />
                <img src={require("../styles/login/images/slide (2).jpg")} alt="slide image" />
                <img src={require("../styles/login/images/slide (3).jpg")} alt="slide image" />
                <img src={require("../styles/login/images/slide (4).jpg")} alt="slide image" />
                <img src={require("../styles/login/images/slide (5).jpg")} alt="slide image" />
              </div>
            </div>
            <div className="form-container">
              <div className="form-content box">
                <div className="logo">
                  <img src={require("../styles/login/images/logo-light.png")} alt="Instagram logo" className="logo-light"/>
                  <img src={require("../styles/login/images/logo-dark.png")} alt="Instagram logo" className="logo-dark"/>
                </div>
                <div className="signin-form" id="signin-form">
                  <div className="form-group">
                    <div className="animateinput">
                                              {/*<span>*/}
                                              {/*    Phone number, username or email*/}
                                              {/*</span>*/}
                      <input type="text" placeholder="Phone number, username or email"/>
                    </div>
                  </div>
                  <div className="form-group">
                    <div className="animate-input">
                                              {/*<span>*/}
                                              {/*    Password*/}
                                              {/*</span>*/}
                      <input type="password" placeholder="Password"/>
                      <button>Show</button>
                    </div>
                  </div>
                  <div className="btn-group">
                    <button className="btn-login" id="signin-btn"type="submit" value="Submit">
                      Log In
                    </button>
                  </div>
                  <div className="divine">
                    <div></div>
                    <div>OR</div>
                    <div></div>
                  </div>
                  <div className="btn-group">
                    <button className="btn-fb">
                      <img src={require("../styles/login/images/facebook-icon.png")} alt="" />
                        <span>Log in with Facebook</span>
                    </button>
                  </div>
                  <a href="src/routes/login#" className="forgot-pw">Forgot password?</a>
                </div>
              </div>
              <div className="box goto">
                <p>
                  Don't have an account?
                  <a href="src/routes/login#">Sign up</a>
                </p>
              </div>

              <div className="app-download">
                <p>Get the app.</p>
                <div className="store-link">
                  <a href="src/routes/login#">
                    <img src={require("../styles/login/images/app-store.png")} alt="app store" />
                  </a>
                  <a href="src/routes/login#">
                    <img src={require("../styles/login/images/gg-play.png")} alt="google play" />
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="footer">
          <div className="links">
            <a href="src/routes/login#">About</a>
            <a href="src/routes/login#">Blog</a>
            <a href="src/routes/login#">Jobs</a>
            <a href="src/routes/login#">Help</a>
            <a href="src/routes/login#">API</a>
            <a href="src/routes/login#">Privacy</a>
            <a href="src/routes/login#">Terms</a>
            <a href="src/routes/login#">Top Accounts</a>
            <a href="src/routes/login#">Hashtags</a>
            <a href="src/routes/login#">Locations</a>
            <a href="src/routes/login#" id="darkmode-toggle">Darkmode</a>
          </div>
          <div className="copyright">
            © 2021 Instagram from Facebook
          </div>
        </div>
      </div>
      {/*<script src={require("../styles/login/app.js")}></script>*/}
    </>
  )
}

const mapStateToProps = (state: any) => {
  return {
    userData: state.login
  }
}

const mapDispatchToProps = (dispatch: any) => {
  return {
    login: () => dispatch(login())
  }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Login)
