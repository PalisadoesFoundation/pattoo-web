/* React Imports */
import React from "react";

/* Components Imports */
import Base from "./Base";

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
  const _mainClassName = `mt-${margin} bg-gray-100 shadow-md rounded-lg p-5`;

  return (
    <div className={_mainClassName}>
      <h3 className="text-xs underline">{title}</h3>
      <div className="mt-2">
        {stats.map(({ name, value }) => (
          <div
            key={`entry-${name}`}
            className="flex justify-between text-sm py-4"
          >
            <p className="">{name}</p>
            <p className="text-gray-500 text-xs font-semibold">{value}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

function Chart() {
  return <div className="bg-red-300 mb-8 h-64 shadow-xl"></div>;
}

function DashboardComponent(props) {
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
            <div className="col-start-4 col-end-13">
              <Chart />
              <Chart />
              <Chart />
              <Chart />
              <Chart />
            </div>
          </div>
        </div>
      )}
    />
  );
}

export default DashboardComponent;
