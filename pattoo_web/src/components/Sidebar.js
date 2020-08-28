/* React Imports */
import React, { useState } from "react";
import { Link } from "react-router-dom";

/* Tailwind css build */
import "../styles/main.css";

/* Fontawesome Icons */
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faHome } from "@fortawesome/free-solid-svg-icons";

/* Assets Imports */
import PattooLogo from "../assets/pattoo-light 1.png";

/* Sidebar Components */
function Header() {
  return (
    <div className="py-5 flex justify-between items-center px-5 border-b border-grey-200">
      <img src={PattooLogo} className="object-contain h-16" />
      <p className="text-center text-xs text-gray-600 font-bold">v1.0</p>
    </div>
  );
}

function Nav({ elements, subtitle }) {
  return (
    <div className="flex flex-col mt-5">
      <h3 className="text-indigo-400 tracking-wider uppercase text-xxs font-bold py-2 ml-5">
        {subtitle}
      </h3>
      {elements.map(({ icon, name }) => (
        <NavItem key={name} icon={icon} name={name} />
      ))}
    </div>
  );
}

function NavItem({ icon, name, path }) {
  return (
    <Link to={path}>
      <div className="py-3 mt-5 rounded bg-pattooPrimary mx-2">
        <div className="flex items-center w-1/2 ml-5 ">
          <FontAwesomeIcon icon={icon} size="xs" />
          <span className="ml-5 text-sm text-pattooAccentTwo font-semibold">
            {name}
          </span>
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
  },
  {
    icon: faHome,
    name: "Agents",
    path: "/agents",
  },
];

const controlNav = [
  {
    icon: faHome,
    name: "Settings",
    path: "/settings",
  },
  {
    icon: faHome,
    name: "Themes",
    path: "/themes",
  },
  { icon: faHome, name: "Logout", path: "/login" },
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
    <div className="fixed w-64 h-full shadow-lg">
      <Header />
      <div className="pt-10">
        <Nav
          elements={mainNav}
          subtitle={localStorage.getItem("current_user")}
        />
        <Nav elements={controlNav} subtitle="controls" />
      </div>
    </div>
  );
}

export default Sidebar;
