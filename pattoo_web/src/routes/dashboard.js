/* React Imports */
import React, { useState, useEffect } from "react";

/* Components Import */
import DashboardComponent from "../components/Dashboard";

import queryResource from "../graphql_client";

/* Tailwind css build */
import "../styles/main.css";

function Dashboard() {
  const [chartData, setChartData] = useState({});
  const accessToken = localStorage.getItem("accessToken");

  useEffect(() => {
    const query = `
        query{
            allData(idxDatapoint: "1", token: "${accessToken}"){
                edges{
                    node{
                        value
                        timestamp
                    }
                }
            }
        }
      `;

    queryResource(query)
      .then((result) => setChartData(result.data.data.allData.edges))
      .catch(console.log);
  }, []);
  return <DashboardComponent data={chartData} />;
}

export default Dashboard;
