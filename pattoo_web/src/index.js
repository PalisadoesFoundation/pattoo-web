/* React Imports */
import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";

/* Styles Imports */
import "./styles/main.css";

/* Routes Imports */
import RenderRoutes from "./routes";

function App() {
  return <RenderRoutes />;
}

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById("root")
);
