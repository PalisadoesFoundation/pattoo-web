/* React Imports */
import React, { useState, useEffect } from "react";

/* Components Import */
import DashboardComponent from "../../components/Dashboard";

/* Querying */
import query from "../../utils/query";
import { userFavorite } from "../../utils/api";

/* Tailwind css build */
import "../../styles/main.css";

function parseFavoriteCharts(response) {
  return response.data.data.allFavorite.edges
    .map(
      (
        {
          node: {
            chart: { name, chartDatapointChart },
          },
        },
        index
      ) => {
        return {
          name: name ? name : `Default-Chart-${index}`,
          datapoints: chartDatapointChart.edges.map(
            ({
              node: {
                datapoint: { idxDatapoint, dataChecksum },
              },
            }) => {
              return {
                datapointID: idxDatapoint,
                data: dataChecksum.edges.map(
                  ({ node: { value, timestamp } }) => ({ value, timestamp })
                ),
              };
            }
          ),
        };
      }
    )
    .filter(({ datapoints }) => datapoints.length != 0); // Filters out datapoints with empty data
}

function Dashboard() {
  const [chartData, setChartData] = useState([]);
  const token = localStorage.getItem("accessToken");
  const userID = localStorage.getItem("userID");

  useEffect(() => {
    query(userFavorite(userID, token))
      .then((response) => setChartData(parseFavoriteCharts(response)))
      .catch(console.log);
  }, []);
  return <DashboardComponent data={chartData} />;
}

export default Dashboard;
