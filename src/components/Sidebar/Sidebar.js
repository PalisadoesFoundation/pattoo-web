/* React Imports */
import React from "react";

import "../../styles/main.css";
import SidebarItem from "../SidebarItem/SidebarItem";

let sidebarItems=['Dashboard', 'Agents', 'Favorites', 'Settings'];

function Sidebar() {
    return (
        <div id="sidebar" className="h-screen md:w-64 lg:w-64 hidden md:block lg:block bg-gray-800">
            <div className="flex w-full h-16 bg-gray-800 font-bold text-white text-2xl items-center justify-around">
                Pattoo
            </div>

            <p className="px-4 py-2 font-bold text-white">Main</p>
            <ul className="flex flex-col">
                {sidebarItems.map((text,index) => (
                    <SidebarItem text={text} key={index} />
                ))}
            </ul>

        </div>
    );
}

export default Sidebar;


//            TODO
//add "X" to close menu and reveal hamburger icon
//add profile section - profileDesign.png
