/* React Imports */
import React from "react";

import "../../styles/main.css";

//replace navigtion links when pages are created

function Header() {
  return (
    <header className="flex w-full px-6 items-center h-16 bg-white shadow-lg z-10">
        <div className="inline-flex px-6 text-gray-800 text-4xl font-bold ">
          Dashboard
        </div>
    </header>
  );
}

export default Header;


//            TODO
//add hamburger option for mobile
//add pattoo logo 
//add logout button
