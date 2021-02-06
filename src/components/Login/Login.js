/* React Imports */
import React, { useState } from "react";
// import { useHistory } from "react-router-dom";

/* Authentication method imports */
// import { authenticate } from "../../utils/query";

/* CSS Imports */
import "./Login.css";

function Login() {
  // const history = useHistory();
  const [formState, setFormState] = useState({
    username: "",
    password: "",
  });
  return (
    <div id="login" className="flex h-screen justify-center items-center">
      <div id="logo">
        <img src="assets/pattoo-light.png" alt="login" className="w-18"></img>
      </div>
      <form>
        <input
          className=""
          type="text"
          placeholder="Username"
          value={formState.username}
          onChange={(e) => {
            setFormState({
              ...formState,
              username: e.target.value,
            });
          }}
        ></input>
        <input
          className=""
          type="password"
          placeholder="Password"
          value={formState.password}
          onChange={(e) => {
            setFormState({
              ...formState,
              password: e.target.value,
            });
          }}
        ></input>
      </form>
      <button className="bg-purple-900 hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-full">
        Sign in Now
      </button>
      <p className="font-bold mt-5 text-purple-900">
        <a
          href="."
          className="font-normal  hover:text-blue-500 text-blue-700 mr-1"
        >
          Forgot Password?
        </a>
        Request to reset
      </p>
    </div>
  );
}

export default Login;
