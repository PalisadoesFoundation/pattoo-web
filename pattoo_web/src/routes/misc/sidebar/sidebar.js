import React from "react";
import "./sidebar.css";
import PattooLogo from "./assets/pattoo-light 1.png";
import DashBoardIcon from "./assets/dashboard.png";
import AgentIcon from "./assets/agents.png";

function Sidebar() {
  return (
    <div className="sidebar">
      <div className="section header">
        <img src={PattooLogo} />
        <p className="version">v1.0</p>
      </div>

      <div className="section nav_section">
        <div className="nav_element active">
          <img src={DashBoardIcon} className="icon" />
          <p className="nav_item">Dashboard</p>
        </div>
        <div className="nav_element">
          <img src={AgentIcon} className="icon" />
          <p className="nav_item">Agents</p>
        </div>
      </div>
      <div className="section favorites">3</div>
      <div className="section controls">4</div>
    </div>
  );
}

export default Sidebar;
