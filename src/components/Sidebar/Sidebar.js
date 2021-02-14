/* React Imports */
import React from "react";
import PropTypes from 'prop-types';
import {IconContext} from "react-icons";
import { IoIosArrowBack } from "react-icons/io";
import {MdHome, MdBuild, MdSettings} from "react-icons/md";

import "../../styles/main.css";
import FavoriteItem from "../FavoriteItem/FavoriteItem";
import logo from './pattoo_white_noname.png';

let favoriteItems=[
    {id : 'Tracking OS Performance'     },
    {id : 'Client SNMP Tracking'        },
    {id : 'ATL A/C 1 Power Effciency'   },
    {id : 'ATL A/C 1 Power Effciency'   },
];

function Sidebar({isStatic, setClosed, isClosed}) {
    return (//make custom sidebar width
    
        <aside id="sidebar" className={`flex flex-col w-64 flex-shrink-0 min-h-full bg-gray-800 z-50 ${isStatic ? '' : 'fixed'}`}>
            <div className="flex h-16 bg-gray-800 items-center justify-around">
                <div className="flex items-center justify-center">
                    <img src={logo} alt="Logo" className="h-12 w-auto"/>
                    <p className="text-white font-medium text-xl">Pattoo</p>
                </div>
                {!isStatic  && ( 
                    <button title={"Close menu"} onClick={() => setClosed(true)} className="p-2 bg-gray-500 rounded-md" aria-label={"Close menu"} aria-hidden={!isClosed}>
                        <IconContext.Provider  value={{ size: '24px'}}>
                            <IoIosArrowBack/>
                        </IconContext.Provider>
                    </button>
                )}
            </div>

            <nav>
                <ul>
                    <div>
                        <p className="px-4 py-4 font-bold text-white bg-gray-800">Main</p>
                        <a href="index.html" className="font-sans text-nav-item no-underline">
                            <li className="flex items-center pr-4 pl-8 py-2  text-white hover:bg-gray-700">
                                    <IconContext.Provider value={{ size: '20px'}}><MdHome/></IconContext.Provider>               
                                    <span className="px-2">Dashboard</span>
                            </li>
                        </a>

                        <a href="index.html" className="font-sans text-nav-item no-underline">
                            <li className="flex items-center pr-4 pl-8 py-2 text-white hover:bg-gray-700">
                                    <IconContext.Provider value={{ size: '20px'}}><MdBuild/></IconContext.Provider>               
                                    <span className="px-2">Agents</span>
                            </li>
                        </a>
                    </div> 
                    
                
                    <div className="flex flex-col">
                        <p className="px-4 py-4 font-bold text-white bg-gray-800">Favorites</p>
                        {favoriteItems.map((items,index) => (
                            <FavoriteItem text={items.id} key={index}/>
                        ))}
                    </div>
                    
                    
                    <div className="flex flex-col">
                    <p className="px-4 py-4 font-bold text-white bg-gray-800">Controls</p>
                        <a href="index.html" className="font-sans text-nav-item no-underline">
                            <li className="flex items-center pr-4 pl-8 py-2 text-white hover:bg-gray-700">
                                    <IconContext.Provider  value={{ size: '20px'}}><MdSettings/></IconContext.Provider>               
                                    <span className="px-2">Settings</span>
                            </li>
                        </a>
                    </div>
                </ul>
            </nav>
        </aside>
    );
}

export default Sidebar;

Sidebar.propTypes = {
    isStatic: PropTypes.bool,
    setClosed: PropTypes.func,
    isClosed: PropTypes.bool,
};


//            TODO
//add "X" to close menu and reveal hamburger icon
//add profile section - profileDesign.png
