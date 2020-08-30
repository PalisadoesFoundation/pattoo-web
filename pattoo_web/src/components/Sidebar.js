/* React Imports */
import React, { useState } from "react";
import { Link } from "react-router-dom";
import Modal from "react-modal";

/* Tailwind css build */
import "../styles/main.css";

/* Fontawesome Icons */
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faHome,
  faStar,
  faLayerGroup,
  faCog,
  faPlus,
  faColumns,
} from "@fortawesome/free-solid-svg-icons";

/* Assets Imports */
import PattooLogo from "../assets/pattoo-light 1.png";

/* Sidebar Components */
function Header() {
  const [showModal, setShowModal] = useState(false);
  const updateShowModal = (e) => setShowModal(true);

  return (
    <div className="row-span-1 py-5 flex flex-col justify-between">
      <div className="w-full flex justify-between items-center border-b border-grey-200  p-5">
        <img src={PattooLogo} className="object-contain h-16" />
        <p className="text-center text-xs text-gray-600 font-bold">v1.0</p>
      </div>
      <button
        onClick={updateShowModal}
        className="p-2 mx-2 bg-pattooAccentOne text-sm text-white font-black rounded-md"
      >
        <FontAwesomeIcon icon={faPlus} size="sm" />
        <span className="ml-2">Create New....</span>
      </button>
    </div>
  );
}

function Nav({ elements, subtitle }) {
  return (
    <div className="flex flex-col mt-5">
      <h3 className="text-pattooAccentOne tracking-wider uppercase text-xxs font-bold ml-5">
        {subtitle}
      </h3>
      {elements.map(({ icon, name, active }) => (
        <NavItem key={name} icon={icon} name={name} active={active} />
      ))}
    </div>
  );
}

function NavItem({ icon, name, path, active }) {
  const bgColor = active ? "pattooPrimary" : "";
  const textColor = active ? "text-pattooAccentThree" : "text-gray-600";
  console.log(active);
  return (
    <Link to={path}>
      <div className={`focus:border-none bg-${bgColor} py-3 mt-5 rounded mx-2`}>
        <div className={`flex items-center w-1/2 ml-5 ${textColor}`}>
          <FontAwesomeIcon icon={icon} size="xs" />
          <span className="ml-5 text-sm font-semibold">{name}</span>
        </div>
      </div>
    </Link>
  );
}

function Favorites({ favorites }) {
  return (
    <div className="border-b border-t">
      <div className="h-full flex flex-col justify-between ml-16 py-5">
        {favorites.map((name) => (
          <FavoritesItem key={name} name={name} />
        ))}
        <div className="">
          <span className="text-xs">...Show more</span>
        </div>
      </div>
    </div>
  );
}

function FavoritesItem({ name }) {
  return <span className="text-xs">{name}</span>;
}

const mainNav = [
  {
    icon: faHome,
    name: "Dashboard",
    path: "/dashboard",
    active: true,
  },
  {
    icon: faLayerGroup,
    name: "Agents",
    path: "/agents",
    active: false,
  },
  {
    icon: faStar,
    name: "Favorites",
    path: "/favorites",
    active: false,
  },
];

const controlNav = [
  {
    icon: faCog,
    name: "Settings",
    path: "/settings",
    active: false,
  },
  {
    icon: faColumns,
    name: "Themes",
    path: "/themes",
    active: false,
  },
];

function Sidebar() {
  const [favorites, setFavorites] = useState([
    "Tracking OS Peformance",
    "Client SNMP Tracking",
    "ATL A/C 1 Power Effciency",
    "ATL A/C 2 Power Effciency",
    "Server Power Consumption",
  ]);

  // useEffect to update state of favorite charts, querying graphql
  return (
    <div className="grid grid-rows-12 fixed w-56 h-full shadow-xl">
      <Header />
      <div className="row-span-6 pt-10">
        <Nav elements={mainNav} subtitle="main" />
        <Nav elements={controlNav} subtitle="controls" />
      </div>
      <div className="grid grid-cols-4 gap-2 row-span-1">
        <div className="col-span-1 h-full bg-pattooAccentOne"></div>
        <div className="col-span-2 mt-10">
          <h4 className="text-pattooAccentOne text-sm font-bold">
            {localStorage.getItem("current_user")}
          </h4>
          <button className="text-xxs font-black text-gray-700">
            View Profile
          </button>
        </div>
        <button className="col-span-1 mr-4 text-xxs font-black text-gray-700">
          Logout
        </button>
      </div>
    </div>
  );
}

export default Sidebar;
