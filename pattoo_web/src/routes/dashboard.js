/* React Imports */
import React, { useState, useEffect } from "react";

/* Components Import */
import DashboardComponent from "../components/Dashboard";

/* Querying */
import queryResource from "../graphql_client";
import { userFavorite } from "../api";

/* Tailwind css build */
import "../styles/main.css";

function Dashboard() {
  const [chartData, setChartData] = useState({});
  const token = localStorage.getItem("accessToken");

  useEffect(() => {
    queryResource(userFavorite(token)).then(console.log).catch(console.log);
  }, []);
  return <DashboardComponent data={chartData} />;
}

export default Dashboard;
