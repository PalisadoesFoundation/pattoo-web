/* React Imports */
import React from "react";

import "../../styles/main.css";

//replace navigtion links when pages are created

function Header() {
  return (
    <header className="flex w-full px-6 items-center h-16 bg-gray-900 z-10">
        <div className="inline-flex">
          <h1 className="text-white font-bold">Pattoo</h1>
        </div>
    </header>
  );
}

export default Header;


//            TODO
//add hamburger option for mobile
//add pattoo logo 
//add logout button
