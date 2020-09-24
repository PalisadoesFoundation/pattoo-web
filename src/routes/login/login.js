/* React Imports */
import React, { useState } from "react";
import { useHistory } from "react-router-dom";

/* Authentication method imports */
import { authenticate } from "../graphql_client";

/* Components */
import LoginComponent from "../components/Login";

function Login() {
  const history = useHistory();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const updateLoginField = (e) => setUsername(e.target.value);
  const updatePasswordField = (e) => setPassword(e.target.value);
  const login = async (e) => {
    authenticate(username, password).then((response) => {
      if (response) {
        localStorage.setItem("current_user", username);
        history.push("/");
      } else {
        setUsername("");
        setPassword("");
      }
    });
  };

  return (
    <LoginComponent
      username={username}
      password={password}
      updateLoginField={updateLoginField}
      updatePasswordField={updatePasswordField}
      submission={login}
    />
  );
}

export default Login;
