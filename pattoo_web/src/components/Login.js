/* React Imports */
import React from "react";

/* Styles and Assets Imports */
import "../styles/main.css";
import PattooLogo from "../assets/pattoo-light 1.png";

function LoginComponent({
  username,
  password,
  updateLoginField,
  updatePasswordField,
  submission,
}) {
  return (
    <div className="w-full h-screen flex justify-center sm:flex-none">
      <div className="lg:w-2/5 md:w-4/5 sm:w-full h-auto flex flex-col items-center mt-48">
        <div className="w-full h-auto flex flex-col items-center py-6">
          <img
            src={PattooLogo}
            className="object-contain h-48 xs:h-20 w-full"
          />
        </div>

        <div className="w-1/2 mt-10">
          <input
            type="text"
            placeholder="Login"
            className="w-full border-b-2 pb-2 text-sm text-grey-500 focus:outline-none focus:border-pattooAccentTwo"
            value={username}
            onChange={updateLoginField}
          />
          <input
            type="password"
            placeholder="Password"
            className="mt-8 w-full border-b-2 pb-2 text-sm text-grey-500 focus:outline-none focus:border-pattooAccentTwo"
            value={password}
            onChange={updatePasswordField}
          />
        </div>

        <div className="mt-8 flex flex-col items-center">
          <button
            onClick={submission}
            className="w-2/3 bg-pattooAccentThree uppercase text-sm font-black text-white rounded-full py-5 "
          >
            Sign in now
          </button>
          <p className="mt-5 text-sm text-gray-500">
            <span className="text-pattooAccentOne font-medium">
              Forgot Password?
            </span>
            <a
              href="#"
              className="ml-1 hover:underline font-bold text-pattooAccentThree"
            >
              Request to reset
            </a>
          </p>
        </div>
      </div>
    </div>
  );
}

export default LoginComponent;
