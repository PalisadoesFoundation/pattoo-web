/* React Imports */
import React, { useState } from "react";

/* Authentication method imports */
import { authenticate } from "../graphql_client";

/* Components */
import LoginComponent from "../components/Login";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const updateLoginField = (e) => setUsername(e.target.value);
  const updatePasswordField = (e) => setPassword(e.target.value);

  return (
    <LoginComponent
      username={username}
      password={password}
      updateLoginField={updateLoginField}
      updatePasswordField={updatePasswordField}
      submission={() => authenticate(username, password)}
    />
  );
}

export default Login;
