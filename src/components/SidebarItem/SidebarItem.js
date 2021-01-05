/* React Imports */
import React from "react";

function SidebarItem() {//accepts listitemname as a prop
    return (
        <li className=" w-full h-full py-3 px-2 border-b border-300-border ">
            <a href="index.html" className="font-sans font-hairline hover:font-normal text-sm text-nav-item no-underline">
                Dashboard
            </a>
        </li>
    );
}

export default SidebarItem;
