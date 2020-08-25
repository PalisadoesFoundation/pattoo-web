/* React Imports */
import React from "react";

/* Styles and Assets Imports */
import "../styles/main.css";
import PattooLoginLogo from "../assets/pattoo_login.png";

function LoginComponent({
  username,
  password,
  updateLoginField,
  updatePasswordField,
}) {
  return (
    <div className="border w-full h-screen flex justify-center">
      <div className="w-2/5 h-auto flex flex-col items-center mt-40">
        <div className="w-full h-auto flex flex-col items-center py-6">
          <img src={PattooLoginLogo} className="object-contain h-32 w-full" />
          <h2 className="mt-4 text-3xl font-bold uppercase">Sign in</h2>
          <p className="w-1/2 mt-4 text-md font-medium">
            Hello! Sign in and start managing your Pattoo data!
          </p>
        </div>

        <div className="w-1/2">
          <input
            type="text"
            placeholder="Login"
            className="w-full border-b-2 pb-2 text-sm text-grey-500"
            value={username}
            onChange={updateLoginField}
          />
          <input
            type="password"
            placeholder="Password"
            className="mt-8 w-full border-b-2 pb-2 text-sm text-grey-500"
            value={password}
            onChange={updatePasswordField}
          />
        </div>

        <div className="mt-8 flex flex-col items-center">
          <button className="w-2/3 bg-gray-500 uppercase text-sm font-bold text-white rounded-full py-5">
            Sign in now
          </button>
          <p className="mt-5 text-sm text-gray-500">
            Forgot Password?
            <a href="#" className="ml-1 hover:underline font-bold">
              Request to reset
            </a>
          </p>
        </div>
      </div>
    </div>
  );
}

export default LoginComponent;
