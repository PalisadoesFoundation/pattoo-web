/* React Imports */
import React, { useState } from "react";

/* Tailwind css build */
import "../styles/main.css";

/* Assets Imports */
import PattooLogo from "../assets/pattoo-light 1.png";
import DashBoardIcon from "../assets/dashboard.png";
import AgentIcon from "../assets/agents.png";
import SettingsIcon from "../assets/settings.png";
import ThemesIcon from "../assets/themes.png";
import LogoutIcon from "../assets/logout.png";

/* Sidebar Components */
function Header() {
  return (
    <div className="row-span-1 flex flex-col justify-center border-b border-grey-200">
      <img src={PattooLogo} className="object-contain h-20 w-full" />
      <p className="text-center text-xs text-gray-600 font-bold">v1.0</p>
    </div>
  );
}

function Nav({ elements }) {
  return (
    <div className="row-span-2 flex flex-col justify-center ml-16">
      {elements.map(({ icon, name }) => (
        <NavItem key={name} icon={icon} name={name} />
      ))}
    </div>
  );
}

function NavItem({ icon, name }) {
  return (
    <div className="flex items-center py-5">
      <img src={icon} className="object-contain" />
      <span className="ml-5 text-sm">{name}</span>
    </div>
  );
}

function Favorites({ favorites }) {
  return (
    <div className="row-span-5 border-b border-t">
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
  { icon: DashBoardIcon, name: "Dashboard" },
  { icon: AgentIcon, name: "Agents" },
];

const controlNav = [
  { icon: SettingsIcon, name: "Settings" },
  { icon: ThemesIcon, name: "Themes" },
  { icon: LogoutIcon, name: "Logout" },
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
    <div className="fixed w-64 h-full grid grid-row-12 shadow-lg">
      <Header />
      <Nav elements={mainNav} />
      <Favorites favorites={favorites} />
      <Nav elements={controlNav} />
    </div>
  );
}

export default Sidebar;
