/* React Imports */
import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";

/* Styles Imports */
import "./styles/main.css";

/* Routes Imports */
// import RouteClient from "routes/routeClient";
import Sidebar from "./components/Sidebar/Sidebar";
import Header from "./components/Header/Header";

function App() {
  return(
    <div>
      <Header />
      <Sidebar />
    </div>
  );

}



ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById("root")
);
