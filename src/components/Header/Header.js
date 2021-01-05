/* React Imports */
import React from "react";

import "../../styles/main.css";

//replace navigtion links when pages are created

function Header() {
  return (
    <header className="flex bg-nav bg-gray-900">
        <div className="p-5 inline-flex">
          <h1 className="text-white font-bold">Logo</h1>
        </div>
    </header>
  );
}

export default Header;
