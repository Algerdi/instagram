import React, { useState } from 'react';
import "../styles/register/register.css";

function Register () {
  return(
    <main>
      <div className="page">
        <div className="header">
          <h1 className="logo">Instagram</h1>
          <p>Sign up to see photos and videos from your friends.</p>
          <button><i className="fab fa-facebook-square"></i> Log in with Facebook</button>
          <div>
            <hr />
              <p>OR</p>
            <hr />
          </div>
        </div>
        <div className="container">
          <form action="">
            <input type="text" placeholder="Mobile Number or Email" />
            <input type="text" placeholder="Full Name" />
            <input type="text" placeholder="Username" />
            <input type="password" placeholder="Password" />
            <button>Sign up</button>
          </form>

          <ul>
            <li>By signing up, you agree to our</li>
            <li><a href="">Terms</a></li>
            <li><a href="">Data Policy</a></li>
            <li>and</li>
            <li><a href="">Cookies Policy</a> .</li>
          </ul>
        </div>
      </div>
      <div className="option">
        <p>Have an account? <a href="">Log in</a></p>
      </div>
      <div className="otherapps">
        <p>Get the app.</p>
        <button type="button"><i className="fab fa-apple"></i> App Store</button>
        <button type="button"><i className="fab fa-google-play"></i> Google Play</button>
      </div>
      <div className="footer">
        <ul>
          <li><a href="">ABOUT</a></li>
          <li><a href="">HELP</a></li>
          <li><a href="">PRESS</a></li>
          <li><a href="">API</a></li>
          <li><a href="">JOBS</a></li>
          <li><a href="">PRIVACY</a></li>
          <li><a href="">TEMS</a></li>
          <li><a href="">LOCATIONS</a></li>
          <li><a href="">TOP ACCOUNTS</a></li>
          <li><a href="">HASHTAGS</a></li>
          <li><a href="">LANGUAGE</a></li>
        </ul>
        <p>© 2020 INSTAGRAM</p>
      </div>
    </main>
  )
}

export default Register
