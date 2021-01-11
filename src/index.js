/* React Imports */
import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";

/* Styles Imports */
import "./styles/main.css";

/* Routes Imports */
import Sidebar from "./components/Sidebar/Sidebar";
import Header from "./components/Header/Header";
import Card from "./components/Card/Card";
import Graphcard from "./components/Graphcard/Graphcard";

function App() {
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

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById("root")
);
