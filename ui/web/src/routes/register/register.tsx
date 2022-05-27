import React, { useState } from 'react';
import { Link } from "react-router-dom";
import "../../styles/register/register.css";
import {register} from "../../store/register/registerActions";
import {connect} from "react-redux";

// @ts-ignore
function Register ({userData, register}) {

  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [name, setName] = useState('');
  const [password, setPassword] = useState('');

  const submit = (event: any) => {
    event.preventDefault();
    register(email, username, name, password);
  }

  return(
    <main>
      <div className="page">
        <div className="header">
          <div className="logo">
            <img src={require("../../styles/images/logo-light.png")} alt="Instagram logo" className="logo-light"/>
          </div>
          <p>Sign up to see photos and <br/> videos from your friends.</p>
          <button><i className="fab fa-facebook-square"></i> Log in with Facebook</button>
          <div>
            <hr />
              <p>OR</p>
            <hr />
          </div>
        </div>
        <div className="container">
          <form onSubmit={submit}>
            <input className="input-data" type="text" placeholder="Mobile Number or Email" value={email}
                   onChange={event => setEmail(event.target.value)}/>
            <input className="input-data" type="text" placeholder="Full Name" value={name}
                   onChange={event => setName(event.target.value)}/>
            <input className="input-data" type="text" placeholder="Username" value={username}
                   onChange={event => setUsername(event.target.value)}/>
            <input className="input-data" type="password" placeholder="Password" value={password}
                   onChange={event => setPassword(event.target.value)}/>
            <input className="btn-submit" type="submit" value="Sign up" />
          </form>

          <ul>
            <li>By signing up, you agree to our </li>
            <li><a href="">Terms</a></li>
            <li><a href="">Data <br/> Policy</a></li>
            <li> and </li>
            <li><a href="">Cookies Policy</a> .</li>
          </ul>
        </div>
      </div>
      <div className="option">
        <p>Have an account? <Link to="/login">Log in</Link></p>
      </div>
      <div className="otherapps">
        <p>Get the app.</p>
        <a href="src/routes/login#">
          <img src={require("../../styles/images/app-store.png")} alt="app store" />
        </a>
        <a href="src/routes/login#">
          <img src={require("../../styles/images/gg-play.png")} alt="google play" />
        </a>
      </div>
      <div className="footer">
        <ul>
          <li><a href="">Meta</a></li>
          <li><a href="">About</a></li>
          <li><a href="">Blog</a></li>
          <li><a href="">Jobs</a></li>
          <li><a href="">Help</a></li>
          <li><a href="">API</a></li>
          <li><a href="">Privacy</a></li>
          <li><a href="">Terms</a></li>
          <li><a href="">Top Accounts</a></li>
          <li><a href="">Hashtags</a></li>
          <li><a href="">Locations</a></li>
          <li><a href="">Instagram Lite</a></li>
          <br/>
          <li><a href="">English</a></li>
          <li>© 2020 INSTAGRAM</li>
        </ul>
      </div>
    </main>
  )
}


const mapStateToProps = (state: any) => {
  return {
    userData: state.register
  }
}

const mapDispatchToProps = (dispatch: any) => {
  return {
    register: (email: string, username: string, name: string, password: string) => dispatch(
      register(email, username, name, password)
    )
  }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Register)
