/* Routes configuration */

/* React Imports */
import React from "react";
import { Route, Switch } from "react-router-dom";

/* Route components */
import Login from "./routes/login";
import Dashboard from "./routes/dashboard";

function RenderRoutes() {
  return (
    <Switch>
      <Route path="/login" exact={true} component={Login} />
      <Route path="/dashboard" exact={true} component={Dashboard} />
      <Route path="/" exact={true} component={Dashboard} />
      <Route component={() => <h1>Not Found!</h1>} />
    </Switch>
  );
}

export default RenderRoutes;
