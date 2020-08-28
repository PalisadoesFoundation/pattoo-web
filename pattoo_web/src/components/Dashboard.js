/* React Imports */
import React from "react";

/* Components Imports */
import Base from "./Base";
import { Line } from "react-chartjs-2";

/* Styles and Assets Imports */
import "../styles/main.css";

const dummyStats = [
  {
    title: "Recently Updates",
    stats: [
      { name: "Pattoo Agent Linux", value: "10 mins ago" },
      { name: "Samsung A/C modules", value: "1 hour ago" },
      { name: "nGix Server Metrics", value: "5 mins ago" },
      { name: "OS Modules", value: "10 mins ago" },
      { name: "JSE - Main Market", value: "24 mins ago" },
    ],
  },
  {
    title: "Account Statistics",
    stats: [
      { name: "Files Ingested Today", value: "1000" },
      { name: "Files Ingesterd for Month", value: "10k" },
      { name: "Total Active Agents", value: "10" },
      { name: "Total Tracked Datapoints", value: "100" },
    ],
  },
];

function StatsCard({ title, stats, index }) {
  let margin = 0;
  if (index > 0) {
    margin = 8;
  }

  return (
    <div
      className={`stat-card-height mt-${margin} bg-pattooPrimary shadow-md rounded-lg p-5`}
    >
      <h3 className="text-xs text-pattooAccentThree underline font-semibold">
        {title}
      </h3>
      <div className="mt-2">
        {stats.map(({ name, value }) => (
          <div
            key={`entry-${name}`}
            className="flex justify-between font-semibold text-xs text-pattooAccentTwo py-4"
          >
            <p className="">{name}</p>
            <p className="text-xxs font-semibold">{value}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

function Chart({ chartData }) {
  //let chart_data = [];
  //for (let i = 0; i < 100; i++) chart_data.push(Math.random() * 1000 + 1);
  let labels = [];
  let dataSet = [];

  for (let i = 0; i < chartData.length; i++) {
    labels.push(chartData[i].node.timestamp);
    dataSet.push(chartData[i].node.value);
  }

  console.log(labels);
  console.log(dataSet);
  const data = {
    labels: labels,
    datasets: [
      {
        backgroundColor: "rgba(255,99,132,0.2)",
        borderColor: "rgba(255,99,132,1)",
        borderWidth: 1,
        hoverBackgroundColor: "rgba(255,99,132,0.4)",
        hoverBorderColor: "rgba(255,99,132,1)",
        data: dataSet,
      },
    ],
  };

  const options = {
    maintainAspectRatio: false,
    radius: 0,
    legend: { display: false },
    elements: {
      line: { tension: 0.1 },
      point: {
        radius: 0,
      },
    },
    layout: {
      padding: {
        top: 50,
      },
    },
    scales: {
      xAxes: [
        {
          display: false,
        },
      ],
      yAxes: [
        {
          display: false,
        },
      ],
    },
  };

  return (
    <div className="chart-height rounded-lg mb-8 shadow-xl bg-white">
      <Line data={data} options={options} />
    </div>
  );
}

function DashboardComponent({ data }) {
  console.log(data);
  return (
    <Base
      pageName="Dashboard"
      Component={(props) => (
        <div className="">
          <div className="fixed w-1/6">
            {dummyStats.map(({ title, stats }, index) => (
              <StatsCard
                key={title}
                title={title}
                stats={stats}
                index={index}
              />
            ))}
          </div>
          <div className="grid grid-cols-12">
            <div className="col-start-4 col-end-12">
              <Chart chartData={data} />
              <Chart chartData={data} />
              <Chart chartData={data} />
              <Chart chartData={data} />
              <Chart chartData={data} />
              <Chart chartData={data} />
            </div>
          </div>
        </div>
      )}
    />
  );
}

export default DashboardComponent;
