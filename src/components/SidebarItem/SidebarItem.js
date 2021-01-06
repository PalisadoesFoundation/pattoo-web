/* React Imports */
import React from "react";
import PropTypes from 'prop-types';

function SidebarItem({text}) {//accepts listitemname as a prop
    return (
        <li className=" w-full h-full py-3 px-4 text-white hover:bg-gray-800">
            <a href="index.html" className="font-sans font-normal text-sm text-nav-item no-underline">
                {text}
            </a>
        </li>
    );
}

export default SidebarItem;


SidebarItem.propTypes = {
    text: PropTypes.string
};