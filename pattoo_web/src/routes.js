/* Routes configuration */

/* React Imports */
import React from "react";
import { Route, Switch, Redirect } from "react-router-dom";

/* Route components */
import Login from "./routes/login";
import Dashboard from "./routes/dashboard";

function ProtectedRoute({ component: Component, ...props }) {
  return (
    <Route
      {...props}
      render={(props) => {
        const auth = localStorage.getItem("accessToken");
        const authRefresh = localStorage.getItem("refreshToken");
        if (auth && authRefresh) {
          return <Component {...props} />;
        }
        return <Redirect to="/login" />;
      }}
    />
  );
}

function RenderRoutes() {
  return (
    <Switch>
      <Route
        path="/login"
        exact={true}
        component={() => {
          const auth = localStorage.getItem("accessToken");
          const authRefresh = localStorage.getItem("refreshToken");

          if (auth && authRefresh) {
            return <Redirect to="/" />;
          }
          return <Login />;
        }}
      />
      <ProtectedRoute path="/dashboard" exact={true} component={Dashboard} />
      <ProtectedRoute path="/" exact={true} component={Dashboard} />
      <Route component={() => <h1>Not Found!</h1>} />
    </Switch>
  );
}

export default RenderRoutes;
