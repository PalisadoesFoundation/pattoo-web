/* React Imports */
import React from "react";
import PropTypes from 'prop-types';

function FavoriteItem({text}) {//Render the icon
    return (
        <a href="index.html" className="font-sans text-nav-item no-underline">
            <li className="flex items-center pr-4 pl-8 py-2 text-white hover:bg-gray-700">             
                <span>{text}</span>
            </li>
        </a>
    );
}

export default FavoriteItem;


FavoriteItem.propTypes = {
    text: PropTypes.string,
};