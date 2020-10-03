/* React Imports */
import React from "react";

/* Components Imports */
import Base from "./Base";
import { Line } from "react-chartjs-2";

/* Styles and Assets Imports */
import "../styles/main.css";

const dummyStats = [
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
  return (
    <div className={`stat-card-height mt-8 shadow-card border rounded-lg p-5`}>
      <h3 className="w-full p-5 text-md text-pattooAccentOne font-semibold">
        {title}
      </h3>
      <div className="px-5">
        {stats.map(({ name, value }) => (
          <div
            key={`entry-${name}`}
            className="flex items-center justify-between font-semibold text-xs text-pattooAccentThree py-3"
          >
            <p className="">{name}</p>
            <div className="bg-pattooAccentOne rounded-full h-10 w-10 flex items-center justify-center">
              <span className="text-xxs font-semibold text-white font-bold">
                {value}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function Chart({ title, chartData }) {
  const data = {
    labels: chartData[0].data.map(({ timestamp }) => timestamp),
    datasets: [
      {
        labels: chartData[0].datapointID,
        backgroundColor: "rgba(255,99,132,0.2)",
        borderColor: "rgba(255,99,132,1)",
        fill: true,
        borderWidth: 1,
        hoverBackgroundColor: "rgba(255,99,132,0.4)",
        hoverBorderColor: "rgba(255,99,132,1)",
        data: chartData[0].data.map(({ value }) => value),
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
        top: 150,
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

  // Computing date time between start and end of line chart
  //const date = Date(chartData[0].data[0].timestamp);
  //const date_two = Date(
  //chartData[0].data[chartData[0].data.length - 1].timestamp
  //);
  //console.log(chartData[0].date[0].timestamp);
  //console.log(chartData[0].data[chartData[0].data.length - 1].timestamp);
  //console.log("\n\n");
  return (
    <div className="relative chart-height rounded-lg mb-8 shadow-card border bg-white">
      <div className="">
        <h3 className="absolute mt-12 ml-12 text-xl font-bold text-pattooAccentOne font-main">
          {title}
        </h3>
        <h4></h4>
      </div>
      <Line data={data} options={options} />
    </div>
  );
}

function RecentButton({ text, active }) {
  const bgColor = active ? "pattooAccentThree" : "pattooAccentOne";
  const buttonShadow = active ? "shadow-button" : "";
  return (
    <button
      className={`bg-${bgColor} text-white font-bold ${buttonShadow} rounded py-2 mt-6`}
    >
      {text}
    </button>
  );
}

function DashboardComponent({ data }) {
  return (
    <Base
      pageName="Dashboard"
      Component={() => (
        <div className="">
          <div className="fixed w-1/5">
            <div className="stat-card-height shadow-card border rounded-lg p-5">
              <h2 className="w-full p-5 text-md text-pattooAccentOne font-semibold">
                Recently Updated
              </h2>
              <div className="flex flex-col w-full px-5">
                <RecentButton text="Favorites" active={true} />
                <RecentButton text="Charts" active={false} />
                <RecentButton text="Agents" active={false} />
              </div>
            </div>
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
            <div className="col-start-4 col-end-12 ml-8">
              {data.map(({ name, datapoints }) => (
                <Chart key={name} title={name} chartData={datapoints} />
              ))}
            </div>
          </div>
        </div>
      )}
    />
  );
}

export default DashboardComponent;
