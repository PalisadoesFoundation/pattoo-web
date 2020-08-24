/* React Imports */
import React from "react";

/* Components Import */
import Sidebar from "../components/sidebar";

/* Tailwind css build */
import "../styles/main.css";

function StatsColumn({ header, stats }) {
  return (
    <div className="">
      <p>{header}</p>
      {stats.map(({ key, value }) => (
        <StatItem key={key} key_index={key} value={value} />
      ))}
    </div>
  );
}

function StatItem({ key_index, value }) {
  return <div className=""></div>;
}

function Dashboard() {
  return (
    <div className="Dashboard">
      <Sidebar />
      <div className="p-8"></div>
    </div>
  );
}

export default Dashboard;
