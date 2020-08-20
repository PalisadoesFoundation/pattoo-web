import React, { useState } from "react";
import "./login.css";
import PattooLogo from "./assets/pattoo-light 1.png";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const updateLoginField = (e) => setUsername(e.target.value);
  const updatePasswordField = (e) => setPassword(e.target.value);

  return (
    <div className="login">
      <div className="container">
        <div className="header">
          <div className="header_box">
            <img src={PattooLogo} />
          </div>
          <div className="header_box">
            <h2>Sign in</h2>
          </div>
          <div className="header_box">
            <p>Hello! Sign in and start managing your Pattoo data!</p>
          </div>
        </div>

        <div className="credentials">
          <input
            type="text"
            placeholder="Login"
            value={username}
            onChange={updateLoginField}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={updatePasswordField}
          />
        </div>

        <div className="button_group">
          <button className="sign_up_button">Sign in now</button>
          <p className="request_password">
            Forgot Password?
            <a href="#" className="request_password_link">
              Request to reset
            </a>
          </p>
        </div>
      </div>
    </div>
  );
}

export default Login;
