/* React Imports */
import React, { useState } from "react";
import { Link, useHistory } from "react-router-dom";
import Modal from "react-modal";

/* API queries */
import queryResource from "../graphql_client";
import { createChart, createFavorite, createDatapoint } from "../api";

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

// Binding React Modal to public/index.html 'modal' element
Modal.setAppElement("#modal");
Modal.defaultStyles.overlay.backgroundColor = "rgba(240, 244, 255, 0.5)";

/* Sidebar Components */
function Header() {
  const [chartTitle, setChartTitle] = useState("");
  const [datapointID, setDatapointID] = useState("");
  const [enabled, setEnabled] = useState(1);
  const [favorite, setFavorite] = useState(0);

  const clearFields = () => {
    setChartTitle("");
    setDatapointID("");
    setEnabled(1);
    setFavorite(0);
  };

  const [showModal, setShowModal] = useState(false);
  const updateShowModal = () => setShowModal(true);
  const closeModal = () => setShowModal(false);

  const accessToken = localStorage.getItem("accessToken");
  const userID = localStorage.getItem("userID");
  const chartSubmission = () => {
    queryResource(
      createChart(chartTitle, `Checksum-${chartTitle}`, enabled, accessToken)
    )
      .then((response) => {
        const chartID = response.data.data.createChart.chart.idxChart;
        queryResource(
          createDatapoint(datapointID, chartID, enabled, accessToken)
        ).then((response) => {
          // Setups favorite
          if (favorite === 1) {
            const chartID =
              response.data.data.createChartDataPoint.chartDatapoint.idxChart;
            queryResource(
              createFavorite(userID, chartID, "1", enabled, accessToken)
            );
          }
        });

        closeModal();
        clearFields();
      })
      .catch(console.log);
  };

  return (
    <div className="row-span-1 py-5 flex flex-col justify-between">
      <Modal
        isOpen={showModal}
        onRequestClose={closeModal}
        shouldCloseOnOverlayClick={true}
        className={`container mx-auto mt-56 rounded-lg shadow-card bg-white w-1/4 p-16 focus:border-none`}
      >
        <h2 className="text-4xl font-main font-bold text-pattooAccentOne">
          Create Chart
        </h2>
        <div className="mt-5">
          <div className="w-full">
            <h4 className="text-lg text-pattooAccentThree">Chart Title</h4>
            <input
              type="text"
              className="mt-2 text-sm text-pattooAccentOne p-2 w-full border-2 border-pattooAccentOne rounded"
              value={chartTitle}
              onChange={(e) => setChartTitle(e.target.value)}
            />
          </div>
          <div className="flex justify-between mt-5">
            <div className="">
              <h4 className="text-lg text-pattooAccentThree">Datapoint ID</h4>
              <input
                type="number"
                className="mt-2 text-sm text-pattooAccentOne p-2 border-2 border-pattooAccentOne rounded"
                value={datapointID}
                onChange={(e) => setDatapointID(e.target.value)}
              />
            </div>
            <div className="w-1/2 flex flex-col items-center justify-center">
              <div className="flex">
                <input
                  type="checkbox"
                  value={enabled}
                  checked={enabled}
                  onClick={() => setEnabled(enabled === 1 ? 0 : 1)}
                />
                <label className="ml-5">Enabled</label>
              </div>
              <div className="flex">
                <input
                  type="checkbox"
                  value={favorite}
                  checked={favorite}
                  onClick={() => setFavorite(favorite === 1 ? 0 : 1)}
                />
                <label className="ml-5">Favorite</label>
              </div>
            </div>
          </div>
          <div className="grid grid-cols-9 mt-10">
            <button
              className="col-start-1 col-end-5 py-4 border-2 border-pattooAccentOne text-pattooAccentThree"
              onClick={clearFields}
            >
              Clear
            </button>
            <button
              onClick={chartSubmission}
              className="col-start-6 col-end-10 py-4 bg-pattooAccentOne text-white rounded"
            >
              Create
            </button>
          </div>
        </div>
      </Modal>

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
          <span className="ml-5 text-sm font-bold">{name}</span>
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
