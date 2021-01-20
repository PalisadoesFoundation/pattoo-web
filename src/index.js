/* React Imports */
import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Switch, Route, Redirect } from "react-router-dom";

/* Styles Imports */
import "./styles/main.css";

/* Component Imports */
import Dashboard from "./components/Dashboard/Dashboard";
import Login from "./components/Login/Login";

function App() {
  // Temporary routing until authentication is complete
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/dashboard" component={Dashboard}></Route>
        <Route path="/login" component={Login}></Route>
        <Route path="/">
          <Redirect to="/dashboard"></Redirect>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
