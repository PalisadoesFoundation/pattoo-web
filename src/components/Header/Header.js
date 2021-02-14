/* React Imports */
import React from "react";
import PropTypes from 'prop-types';
import {IconContext} from "react-icons";
import {MdMenu} from "react-icons/md";
import { IoIosLogOut } from "react-icons/io";

import "../../styles/main.css";

//replace navigtion links when pages are created

function Header({label, name, title, setClosed, isClosed, isStatic}) {
  return (
    <header className="flex justify-between	w-full px-6 items-center h-16 bg-white text-white shadow-lg z-10">{/*text color here affects the icon color*/}
      
      <IconContext.Provider  value={{ size: '24px'}}>
      {(!isStatic && isClosed) && ( 
        <button title={"Open menu"} onClick={() => setClosed(false)} className="p-2 bg-gray-500 rounded-md" aria-label={"Open menu"}>
          <MdMenu/>
        </button>
      )}
      </IconContext.Provider>

        <div className="inline-flex px-6 text-gray-800 text-4xl font-bold ">
          {label}
        </div>

        <div className="flex items-center h-full">
          <div className="flex-shrink-0 h-10 w-10">
            <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" className="h-10 w-10 rounded-full" alt="profile"/>
          </div>
          <div className={`ml-2 flex-shrink ${isStatic ? '' : 'hidden'}`}>
              <p className="text-sm leading-5 font-medium text-gray-900">{name}</p>
              <p className="text-sm leading-5 text-gray-500">{title}</p>
          </div>
          <div>
            <a href="index.html">
              <button className="bg-gray-800 text-white border font-bold p-2 rounded-md ml-4 shadow">
              <IconContext.Provider  value={{ size: '24px'}}>
                <IoIosLogOut />
              </IconContext.Provider>
              </button>
            </a>
          </div>
        </div>
    </header>
  );
}

export default Header;

Header.propTypes = {
  label: PropTypes.string,
  name: PropTypes.string,
  title: PropTypes.string,
  setClosed: PropTypes.func,
  isClosed: PropTypes.bool,
  isStatic: PropTypes.bool,
};

//            TODO
//add hamburger option for mobile
//add pattoo logo 
//add logout button
