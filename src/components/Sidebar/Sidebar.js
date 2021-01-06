/* React Imports */
import React from "react";

import "../../styles/main.css";

function Sidebar() {
    return (
        <div id="sidebar" className="bg-side-nav w-1/2 md:w-1/6 lg:w-1/6 border-r border-side-nav hidden md:block lg:block">

            <ul className="list-reset flex flex-col">

                <li className=" w-full h-full py-3 px-2 border-b border-300-border ">
                    <a href="index.html" className="font-sans font-hairline hover:font-normal text-sm text-nav-item no-underline">
                        Dashboard
                    </a>
                </li>

                <li className="w-full h-full py-3 px-2 border-b border-300-border">
                    <a href="index.html" className="font-sans font-hairline hover:font-normal text-sm text-nav-item no-underline">
                        Agents
                    </a>
                </li>

                <li className="w-full h-full py-3 px-2 border-b border-300-border">
                    <a href="index.html" className="font-sans font-hairline hover:font-normal text-sm text-nav-item no-underline">
                        Favorite
                    </a>
                </li>

                <li className="w-full h-full py-3 px-2 border-b border-light-border">
                    <a href="index.html" className="font-sans font-hairline hover:font-normal text-sm text-nav-item no-underline">
                        Settings
                    </a>
                </li>
            
            </ul>

        </div>
    );
}

export default Sidebar;
