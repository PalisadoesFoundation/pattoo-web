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
  const imgStyle = {
    width: "75px",
    height: "80px",
  };

  return (
    <div className="col-span-8 row-span-1 flex flex-col items-center pt-8">
      <img src={PattooLogo} style={imgStyle} className="flex-1" />
      <p className="flex-1 text-xs text-gray-600">v1.0</p>
    </div>
  );
}

function Nav({ elements }) {
  return (
    <div className="flex flex-col justify-around col-span-8 row-span-1 border pt-2 pb-2">
      {elements.map(({ icon, name }) => (
        <NavItem key={name} icon={icon} name={name} />
      ))}
    </div>
  );
}

function NavItem({ icon, name }) {
  const iconStyle = {
    width: "15px",
    height: "15px",
  };
  return (
    <div className="grid grid-cols-12 cursor-pointer">
      <div className="col-start-3 flex items-center">
        <img src={icon} className="" style={iconStyle} />
        <p className="ml-4">{name}</p>
      </div>
    </div>
  );
}

function Favorites({ favorites }) {
  return (
    <div className="grid grid-cols-8 border pt-8 col-span-8 row-span-5">
      {favorites.map((name) => (
        <div key={name} className="col-start-2 col-span-8 text-xs ml-4">
          <span className="cursor-pointer">{name}</span>
        </div>
      ))}
      <div className="col-start-2 col-span-8 text-xs ml-4">
        <span className="cursor-pointer">...Shore more</span>
      </div>
    </div>
  );
}

function Separator({ titleOn, title }) {
  return <p>Hello World</p>;
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
    <div className="grid grid-cols-8 grid-rows-12 h-full w-1/6 fixed shadow-xl">
      <Header />
      <Nav elements={mainNav} />
      <Favorites favorites={favorites} />
      <Nav elements={controlNav} />
    </div>
  );
}

export default Sidebar;
