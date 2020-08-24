/* React Imports */
import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";

/* Styles Imports */
import "./styles/index.css";

/* Component Imports */
import Dashboard from "./routes/dashboard";
import Login from "./routes/login";

function App() {
  return (
    <div className="App">
      <Login />
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
