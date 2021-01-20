/* React Imports */
import React from "react";

/* User module imports */
import Sidebar from "../Sidebar/Sidebar";
import Header from "../Header/Header";
import Card from "../Card/Card";
import Graphcard from "../Graphcard/Graphcard";

/* Querying */
// import query from "utils/query";
// import { userFavorite } from "utils/api";

/* Importing Styles*/
import "../../styles/main.css";

function Dashboard() {
  //Dashboard Page
  return (
    <div className="flex min-h-screen min-w-screen">
      <Sidebar />
      <div id="main-content" className="w-full">
        <Header />
        <div id="body" className="flex bg-gray-200 w-full h-full">
          <div>
            <Card />
            <Card />
          </div>

          <div>
            <Graphcard />
            <Graphcard />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
