import React, { useState } from 'react';
import { connect } from 'react-redux';
import { Link } from "react-router-dom";
import { login } from '../../store/login/loginActions';
import "../../styles/login/login.css";
import background from "../../styles/images/phone-frame.png";

// @ts-ignore
function Login ({ userData, login }) {

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const submit = (event: any) => {
    event.preventDefault();
    login(email, password);
  }

  return (
    <>
      <div className="container">
        <div className="main-container">
          <div className="main-content">
            <div className="slide-container" style={{ backgroundImage: `url(${background})` }}>
              <div className="slide-content" id="slide-content">
                <img src={require("../../styles/images/slide (1).jpg")} alt="slide image" className="active" />
                <img src={require("../../styles/images/slide (2).jpg")} alt="slide image" />
                <img src={require("../../styles/images/slide (3).jpg")} alt="slide image" />
                <img src={require("../../styles/images/slide (4).jpg")} alt="slide image" />
                <img src={require("../../styles/images/slide (5).jpg")} alt="slide image" />
              </div>
            </div>
            <div className="form-container">
              <div className="form-content box">
                <div className="logo">
                  <img src={require("../../styles/images/logo-light.png")} alt="Instagram logo" className="logo-light"/>
                  <img src={require("../../styles/images/logo-dark.png")} alt="Instagram logo" className="logo-dark"/>
                </div>
                <form onSubmit={submit}>
                <div className="signin-form" id="signin-form">
                  <div className="form-group">
                    <div className="animate-input">
                      <input type="text" placeholder="Phone number, username or email" value={email}
                             onChange={event => setEmail(event.target.value)} />
                    </div>
                  </div>
                  <div className="form-group">
                    <div className="animate-input">
                      <input type="password" placeholder="Password" value={password}
                             onChange={event => setPassword(event.target.value)} />
                      <button>Show</button>
                    </div>
                  </div>
                  <div className="btn-group">
                    <input className="btn-login" type="submit" value="Log in" />
                  </div>
                  <div className="divine">
                    <div></div>
                    <div>OR</div>
                    <div></div>
                  </div>
                  <div className="btn-group">
                    <button className="btn-fb">
                      <img src={require("../../styles/images/facebook-icon.png")} alt="" />
                        <span>Log in with Facebook</span>
                    </button>
                  </div>
                  <a href="src/routes/login#" className="forgot-pw">Forgot password?</a>
                </div>
                </form>
              </div>
              <div className="box goto">
                <p>
                  Don't have an account?
                  <Link to="/register">Sign up</Link>
                </p>
              </div>

              <div className="app-download">
                <p>Get the app.</p>
                <div className="store-link">
                  <a href="src/routes/login#">
                    <img src={require("../../styles/images/app-store.png")} alt="app store" />
                  </a>
                  <a href="src/routes/login#">
                    <img src={require("../../styles/images/gg-play.png")} alt="google play" />
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div className="footer">
          <div className="links">
            <a href="">About</a>
            <a href="">Blog</a>
            <a href="">Jobs</a>
            <a href="">Help</a>
            <a href="">API</a>
            <a href="">Privacy</a>
            <a href="">Terms</a>
            <a href="">Top Accounts</a>
            <a href="">Hashtags</a>
            <a href="">Locations</a>
            <a href="" id="darkmode-toggle">Darkmode</a>
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
    login: (email: string, password: string) => dispatch(login(email, password))
  }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Login)
